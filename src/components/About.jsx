// maybe add a projects page?

//----------------------------------------------------------------
// #Icons
import {
    FaPython,
    FaReact,
    FaUikit,
    FaBootstrap,
    FaNode,
    FaSass,
} from "react-icons/fa";
import { IoLogoJavascript } from "react-icons/io";
import {
    SiPowershell,
    SiPostgresql,
    SiPostman,
    SiExpress,
    SiDocker
} from "react-icons/si";
import "../Assets/BeekeeperLogopng.png";
//----------------------------------------------------------------

function About() {
    return (
        <div className="about-container">
            <div className="bio">
                <img
                    src={require("../Assets/headshot-small.jpg")}
                    alt="heashot"
                    className="headshot"
                />
                <p className="about-paragraph">
                    I spent of the first 10 years of my career journey as a
                    Directory of Photography, but moved into the Development
                    world in 2022. I love building beautiful solutions to
                    complex problems and creating things that have never been
                    seen before.
                    <br />
                    I'm inspired by automation or anything new and interesting.
                    I aspire to build projects that are well used and loved.
                    Also, eventually working on virtual cinematography projects.
                </p>
            </div>
            <div className="languages-container">
                <h5 className="about-title"> Main Languages : </h5>
                <span className="tech-sub-container tech-about-main">
                    <FaPython className="about-icon-main" />
                    Python
                </span>
            </div>
            {/* languages ends ^^^^^^^^^^^^^ */}
            <div className="tech-container">
                <div className="frontend-container">
                    <h5 className="about-title"> Frontend : </h5>
                    <span className="tech-sub-container tech-about-main">
                        <IoLogoJavascript className="about-icon-main" />
                        JavaScript
                    </span>
                    <span className="tech-sub-container">
                        <FaReact className="about-icon" />
                        React
                    </span>
                    <span className="tech-sub-container">
                        <FaSass className="about-icon" />
                        Sass
                    </span>
                    <span className="tech-sub-container">
                        <FaUikit className="about-icon" />
                        UiKit
                    </span>
                    <span className="tech-sub-container">
                        <FaBootstrap className="about-icon" />
                        Bootstrap
                    </span>
                    <span className="tech-sub-container">
                        <img
                            src={require("../Assets/logo-kivy-black.png")}
                            alt="kivy"
                            className="about-icon-manual"
                        />
                        Kivy
                    </span>
                    <span className="tech-sub-container">
                        <img
                            src={require("../Assets/pyscript-sticker-black.png")}
                            alt="kivy"
                            className="about-icon-manual"
                        />
                        Pyscript
                    </span>
                </div>
                {/* FrontEnd Ends ^^^^^^^^^^^^^^^^^^^^ */}
                {/* API/Backend Starts */}
                <div className="api-container">
                    <h5 className="about-title"> Api & Backend: </h5>
                    <span className="tech-sub-container">
                        <FaNode className="about-icon" />
                        Node
                    </span>
                    <span className="tech-sub-container">
                        <img
                            src={require("../Assets/fastapi-png.png")}
                            alt="fast api"
                            className="about-icon-manual"
                        />
                        FastAPI
                    </span>
                    <span className="tech-sub-container">
                        <SiPostgresql className="about-icon" />
                        PostgreSql
                    </span>
                    <span className="tech-sub-container">
                        <SiExpress className="about-icon" />
                        Express
                    </span>
                    <span className="tech-sub-container">
                        <SiPowershell className="about-icon" />
                        PowerShell
                    </span>
                    <span className="tech-sub-container">
                        <SiPostman className="about-icon" />
                        Postman
                    </span>
                    <span className="tech-sub-container">
                        <img
                            src={require("../Assets/BeekeeperLogopng-black.png")}
                            alt="beekeeper"
                            className="about-icon-manual"
                        />
                        Beekeeper
                    </span>
                    <span className="tech-sub-container">
                        <SiDocker className="about-icon" />
                        Docker
                    </span>
                </div>
                {/* API/Backend ends ^^^^^^^^^^^^^^ */}
            </div>
        </div>
    );
}

export default About;
