import React, {Component} from 'react';
import {BrowserRouter, Route} from 'react-router-dom';
import Puzzle from './components.js'


class Controller extends Component {
    render() {
        return (
            <BrowserRouter>
                <div>
                    <div>
                        <Route exact={true} path='/' render={ () => ( <div> <Puzzle/> </div> )}/>
                    </div>
                </div>
            </BrowserRouter>
        ); //End Return
    } //End Render
} //End Controller

export default Controller;
