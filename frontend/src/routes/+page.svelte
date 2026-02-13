<script lang="ts">
    import { onMount } from "svelte";
    import { fetchActivities } from "$lib/api";
    import type { Activity } from "$lib/types";
    import Stopwatch from "$lib/components/Stopwatch.svelte";

    // State: Starts as an empty array
    let activities = $state<Activity[]>([]);
    let error = $state<string | null>(null);

    // Effect: Runs once when the component mounts
    onMount(async () => {
        try {
            activities = await fetchActivities();
        } catch (e) {
            error = "Could not connect to the Terminal Backend.";
            console.error(e);
        }
    });
</script>

<main>
    <h1>// Session Log</h1>
    <Stopwatch />

    {#if error}
        <p style="color: red;">ERROR: {error}</p>
    {:else if activities.length === 0}
        <p>Initializing...</p>
    {:else}
        <ul>
            {#each activities as activity}
                <li style="color: {activity.colour}">
                    [{activity.name}]
                </li>
            {/each}
        </ul>
    {/if}
</main>

<style>
    :root {
        --bg-color: #050507;
        --accent-blue: #007AFF;
        --card-bg: rgba(255, 255, 255, 0.03);
        --border-subtle: rgba(255, 255, 255, 0.08);
        --text-primary: #ffffff;
        --text-secondary: #94a3b8;
    }

    main {
        background-color: var(--bg-color);
        /* Subtle techy grid background */
        background-image: radial-gradient(circle at 2px 2px, rgba(255,255,255,0.02) 1px, transparent 0);
        background-size: 40px 40px;
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        min-height: 100vh;
        padding: 4rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h1 {
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin-bottom: 0.5rem;
        background: linear-gradient(180deg, #fff 0%, #888 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    main::before {
        content: "SYSTEM_ACTIVE // VER 2.0.26";
        font-family: monospace;
        font-size: 0.7rem;
        letter-spacing: 0.3rem;
        color: var(--accent-blue);
        margin-bottom: 1rem;
        opacity: 0.8;
    }

    ul {
        list-style: none;
        padding: 0;
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
        gap: 1.5rem;
        margin-top: 4rem;
        width: 100%;
        max-width: 1000px;
    }

    li {
        background: var(--card-bg);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid var(--border-subtle);
        backdrop-filter: blur(12px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: left;
        font-weight: 500;
        position: relative;
        overflow: hidden;
    }

    /* Hover effect: Glow and Border */
    li:hover {
        transform: translateY(-8px);
        border-color: rgba(0, 122, 255, 0.4);
        background: rgba(255, 255, 255, 0.05);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 
                    0 0 20px rgba(0, 122, 255, 0.1);
    }

    /* Subtle corner accent for that "tech" feel */
    li::after {
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        width: 40px;
        height: 40px;
        background: linear-gradient(45deg, transparent 50%, rgba(255,255,255,0.05) 50%);
    }

    li span {
        display: block;
        color: var(--text-secondary);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.1rem;
        margin-bottom: 0.5rem;
    }

    li:hover span {
        color: var(--accent-blue);
    }
</style>