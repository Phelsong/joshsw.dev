import {Routes, Route} from 'react-router-dom';
import {About} from './index'
//----------------------------------------------------------------

function Main() {
    return (
      <div className="main-container"> 
      main content
        <Routes>
            <Route path="/" element={<About />} />
      </Routes>
      </div>
    );
  }
  
  export default Main;