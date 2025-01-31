import React from 'react';
import ReactDOM from 'react-dom';
import './pages/styles.css';
import App from './pages/App';
import reportWebVitals from './reportWebVitals';

import {createStore, StoreProvider} from "easy-peasy";
import elements from "./store/elementStore";

const elementStore = createStore(elements)

ReactDOM.render(
  <React.StrictMode>
    <StoreProvider store={elementStore}>
        <App />
    </StoreProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
