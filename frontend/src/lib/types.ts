export interface Activity{
    id: string;
    name: string;
    colour: string;

}

export interface Session{
    id:string;
    activity_id:string;
    description:string;
    start_timeL:string;
    end_time:string | null;


}