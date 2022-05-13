import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router } from "react-router-dom";
import './Style/index.css'
import App from './App';
//----------------------------------------------------------------
import UIkit from 'uikit';
import Icons from 'uikit/dist/js/uikit-icons.min.js';
UIkit.use(Icons);
//----------------------------------------------------------------

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <App />
  </Router>
);

