<script lang="ts">
    import { formatTime } from "$lib/utils";

    let isRunning = $state(false);
    let elapsed = $state(0);
    let interval: number;

    function toggleTimer() {
        if (isRunning) {
            isRunning = false;
            clearInterval(interval);
        } else {
            isRunning = true;
            interval = setInterval(() => {
                elapsed += 1;
            }, 1000);
        }
    }
    let displayTime = $derived(formatTime(elapsed));
</script>

<div class="stopwatch-container">
    <div class="time-display">
        {displayTime}
    </div>

    <button onclick={toggleTimer} class={isRunning ? "active" : ""}>
        [{isRunning ? "STOP" : "START"}]
    </button>
</div>

<style>
    :root {
        --bg-color: #0a0a0c;
        --card-bg: rgba(255, 255, 255, 0.03);
        --accent-color: #007AFF; /* Electric Blue */
        --text-main: #ffffff;
        --text-dim: #848486;
        --border-color: rgba(255, 255, 255, 0.1);
    }

    .stopwatch-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2rem;
        padding: 3rem;
        margin-top: 2rem;
        
        background: var(--card-bg);
        backdrop-filter: blur(12px);
        border: 1px solid var(--border-color);
        border-radius: 24px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        max-width: 400px;
        transition: all 0.3s ease;
    }

    .time-display {
        font-size: 4rem;
        font-weight: 700;
        /* Tabular numbers prevent the clock from "jumping" as digits change */
        font-variant-numeric: tabular-nums;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: var(--text-main);
        letter-spacing: -2px;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
    }

    .controls {
        display: flex;
        gap: 1rem;
    }

    button {
        background: var(--accent-color);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.9rem;
        letter-spacing: 0.05rem;
        cursor: pointer;
        transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.2s;
        box-shadow: 0 4px 15px rgba(0, 122, 255, 0.3);
    }

    button:hover {
        transform: scale(1.05);
        filter: brightness(1.1);
    }

    button:active {
        transform: scale(0.95);
    }

    /* Secondary/Reset style button */
    button.secondary {
        background: rgba(255, 255, 255, 0.08);
        color: var(--text-main);
        box-shadow: none;
    }

    .active {
        color: var(--accent-color);
        text-shadow: 0 0 30px rgba(0, 122, 255, 0.4);
    }

    /* Subtle techy indicator */
    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--text-dim);
        margin-bottom: -0.5rem;
    }

    .active .status-dot {
        background: var(--accent-color);
        box-shadow: 0 0 8px var(--accent-color);
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.4; }
        100% { opacity: 1; }
    }
</style>
