import {Routes, Route} from 'react-router-dom';
import {About, Projects} from './index'
//----------------------------------------------------------------

function Main() {
    return (
      <div className="main-container"> 
        <Routes>
            <Route path="/" element={<About />} />
            <Route path="/about" element={<About />} />
            <Route path="/projects" element={<Projects />} />
      </Routes>
      </div>
    );
  }
  
  export default Main;