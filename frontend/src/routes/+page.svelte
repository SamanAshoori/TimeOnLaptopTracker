<script lang="ts">
    import { onMount } from 'svelte';
    import { fetchActivities } from '$lib/api';
    import type { Activity } from '$lib/types';

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
    <h1>Session Log //</h1>

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
    /* Temporary Basic Styles */
    main {
        background-color: #050505;
        color: #00ff41;
        font-family: monospace;
        height: 100vh;
        padding: 2rem;
    }
</style>