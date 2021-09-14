import React from "react";

import Button from "../../components/Button";
import Textbox from "../../components/Textbox";

import axios from "axios";

export default class Home extends React.Component {
    state = {
        input: "",
        lyrics: [],
        disabled: true,
        loading: false
    }

    changeInput = e => {
        this.setState({
            input: e.target.value,
            disabled: e.target.value == ""
        });
    }

    submit = () => {
        const artist = this.state.input;
        const config = {
            method: "POST",
            data: artist
        }

        this.setState({
            loading: true,
            disabled: true
        });

        if (artist !== "") {
            axios.post("http://localhost:5000/", config)
            .then(response => {
                console.log(response);
                this.setState({
                    lyrics: response.data.result,
                    loading: false,
                    disabled: false
                });
            })
            .catch(error => console.log(error));
        } else {
            alert("Empty search query, please enter an artist's name.");
        }
    }

    render() {
        return (
            <div class="page">
                <h1>Enter artist name below to generate lyrics:</h1>
                <div style={{display: "inlineFlex"}}>
                    <Textbox value={this.state.input} onChange={this.changeInput}/>
                    <Button text="Generate" onClick={this.submit} disabled={this.state.disabled}/>
                </div>
                
                <div style={{marginTop: "10vh"}}>
                    {this.state.loading &&
                    <h3>Loading :)</h3>}
                    
                    {this.state.lyrics !== "" && !this.state.loading &&
                    <>{this.state.lyrics.map(lyric => <p>{lyric}</p>)}</>}
                </div>
                
            </div>
        );
    }
}