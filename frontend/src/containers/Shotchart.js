import React, { Component } from 'react';
import { Grid, Container } from 'semantic-ui-react';
import CustomDropdown from '../components/CustomDropdown/CustomDropdown';
import axiosInstance from '../axiosInstance';
import Plot from '../components/Plot/Plot';

class Shotchart extends Component {
    state = {
        seasons: [],
        selectedSeason: null,
        players: [],
        selectedPlayer: null,
        shots: [],
    }

    componentDidMount() {
        axiosInstance.get('/seasons').then(
            resp => {
                this.setState({seasons: resp.data})
            }
        )
    }

    onSeasonSelect = (value) => {
        this.setState({selectedSeason: value});
        axiosInstance.get('/players?season=' + value).then(
            resp => {
                this.setState({players: resp.data})
            }
        )
    }

    onPlayerSelect = (player) => {
        this.setState(
            {
                selectedPlayer: player
            }
        )
    }
    
    render() { 

        const playerOptions = this.state.players.map(
            player => {
                return {
                    key: player["PLAYER_ID"],
                    value: player["PLAYER_ID"],
                    text: player["PLAYER_NAME"]
                }
            }
        );

        return (
            <Container>
                <Grid centered columns={16}>
                    <Grid.Row>
                        <Grid.Column width={8}>
                            <CustomDropdown
                                searchable={false}
                                selectedValue={this.state.selectedSeason}
                                options={this.state.seasons.map(
                                    season => ({key: season, value: season, text: season})
                                )}
                                changed={(event, data) => this.onSeasonSelect(data.value)}/>
                        </Grid.Column>
                        <Grid.Column width={8}>
                            <CustomDropdown
                                searchable={true}
                                options={playerOptions}
                                selectedValue={this.state.selectedPlayer}
                                changed={(event, data) => this.onPlayerSelect(data.value)}/>
                        </Grid.Column>
                    </Grid.Row>
                    <Grid.Row>
                        <Plot
                            playerId={this.state.selectedPlayer}
                            season={this.state.selectedSeason}>
                        </Plot>
                    </Grid.Row>
                </Grid>
            </Container>
        );
    }
}
 
export default Shotchart;