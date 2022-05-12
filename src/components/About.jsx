//----------------------------------------------------------------
// #Icons
import { FaPython, FaReact, FaUikit, FaBootstrap, FaNode, FaHtml5, FaSass, FaWindows} from "react-icons/fa";
import { IoLogoJavascript} from "react-icons/io";
import { SiPowershell, SiFlask, SiPostgresql, SiCss3, SiDjango} from "react-icons/si";
//----------------------------------------------------------------

function About() {
    return (
      <div className="about-container"> 
      <div className="languages-container">
        languages :
        <IoLogoJavascript className="about-icon"/>
        <FaPython className="about-icon"/> 
        <FaHtml5 className="about-icon"/>
        <SiCss3 className="about-icon"/>
        <FaSass className="about-icon"/>
        <SiPostgresql className="about-icon"/>
        <SiPowershell className="about-icon"/>
        </div>
        <div className="frameworks-container">
              frameworks :
              <FaReact className="about-icon" />
              <FaNode className="about-icon"/>
              <SiFlask className="about-icon"/>
              <SiDjango className="about-icon"/>
              <FaUikit className="about-icon"/>
              <FaBootstrap className="about-icon"/>
              <FaWindows className="about-icon"/>
          </div>
      </div>
    );
  }
  
  export default About;