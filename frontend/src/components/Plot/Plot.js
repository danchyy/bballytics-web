import React from 'react';
import axiosInstance from '../../axiosInstance';

const plot = (props) => {
    const queries = [];
    queries.push("playerId=" + props.playerId);
    queries.push("season=" + props.season);
    const queryString = queries.join("&");
    return (
        <div>
            <img src={axiosInstance.defaults.baseURL + "/shotchart?" + queryString} width={640} height={640}></img>
        </div>
    );
}

export default plot;