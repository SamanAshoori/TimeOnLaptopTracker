import type { Activity } from './types';

const API_URL = 'http://127.0.0.1:8000';

export async function fetchActivities(): Promise<Activity[]> {
    const response = await fetch(`${API_URL}/activities`);
    
    if (!response.ok) {
        throw new Error('Failed to fetch activities');
    }
    
    return await response.json();
}