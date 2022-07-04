import { Link } from "react-router-dom";
//----------------------------------------------------------------

function Projects() {
  return (
    <div className="projects-container">
      <div className="projects-sub-container">
        <img
          src={require("../Assets/blueboxsplash.jpg")}
          alt="bluebox"
          className="projects-img"
        />
        <span className="projects-name">BlueBox</span>
        <span className="projects-description">
          Role:
          <br />
          Fullstack Developer
          <br />
          <br />
          Contributions:
          <br />
          I designed the database structure and built out the core cart functionality.
          <br />
          <br />
          Stack:
          <br />
          React | Express | Node | Flask | Postgres
        </span>
        <Link
          to={`//bluebox-atnight.herokuapp.com/`}
          target="_blank"
          uk-icon="link"
        />
        <Link
          to={`//github.com/pjjwGraceShopper/GraceShopper`}
          target="_blank"
          uk-icon="github-alt"
        />
      </div>
      <div className="projects-sub-container">
      <img
          src={require("../Assets/ProjectYnixV1.jpg")}
          alt="project_ynix"
          className="projects-img"
        />
        <span className="projects-name">project_ynix</span>
        <span className="projects-description">
          Role:
          <br />
          Lead Developer
          <br />
          in Development
          <br />
          Goal:
          <br />
          Data Simulation App
          <br />
          <br />
          Stack:
          <br />
          React | Electron | FastAPI
        </span>
        <Link
          to={`//github.com/Phelsong/project-ynix`}
          target="_blank"
          uk-icon="github-alt"
        />
      </div>
      <div className="projects-sub-container">
      <img
          src={require("../Assets/connect-four-splash.jpg")}
          alt="connect-four-splash"
          className="projects-img"
        />
        <span className="projects-name">Connect-Four</span>
        <span className="projects-description">
          Role:
          <br />
          Lead Developer
          <br />
        </span>
        <Link
          to={`//sharp-varahamihira-32ec8e.netlify.app/`}
          target="_blank"
          uk-icon="link"
        />
        <Link
          to={`//github.com/github.com/Phelsong/Arcade-Connect-4`}
          target="_blank"
          uk-icon="github-alt"
        />
      </div>
    </div>
  );
}

export default Projects;
