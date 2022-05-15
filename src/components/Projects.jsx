import {Link} from 'react-router-dom'
//----------------------------------------------------------------

function Projects() {
    return (
      <div className="projects-container"> 
      <div className="projects-sub-container">
        <img src="../Assets/blueboxsplash.jpg" alt="bluebox" className="projects-img"/>
        <span className="projects-name">BlueBox</span>
        <span className="projects-description">
            Role: 
            <br/>
            Fullstack Developer
            <br/>
            I built out the cart...
         </span>
         <Link to={`//bluebox-atnight.herokuapp.com/`} target="_blank" uk-icon="link" />
         <Link to={`//github.com/pjjwGraceShopper/GraceShopper`} target="_blank" uk-icon="github-alt"/>
      </div>
      <div className="projects-sub-container">
      <span className="projects-name">project_ynix</span>
        <span className="projects-description">
            Role: 
            <br/>
            Fullstack Developer
            <br/>
            in Development
         </span>
         <Link to="//github.com/Phelsong/project-ynix" target="_blank" uk-icon="github-alt"/>
          </div>

      </div>
    );
  }
  
  export default Projects;