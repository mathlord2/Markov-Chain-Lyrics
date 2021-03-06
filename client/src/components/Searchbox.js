import React from "react";
import {COLORS, SHADOW} from "../styleVars";
import {FaSearch} from "react-icons/fa";

const Searchbox = props => {
    return (
        <div style={{margin: "0px 10px"}}>
            <FaSearch style={{position: "absolute", marginTop: "14px", marginLeft: "10px", fontSize: "20px"}}/>
            <input placeholder={props.placeholder} value={props.value} onChange={props.onChange} style={{
                padding: "10px",
                paddingLeft: "35px",
                border: "3px solid " + COLORS.primary,
                borderRadius: "15px",
                textAlign: "left",
                width: props.width ? props.width : "20%",
                boxShadow: SHADOW.primary
            }}/>
        </div>
    );
}

export default Searchbox;