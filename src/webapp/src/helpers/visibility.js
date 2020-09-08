export const getVisibilityClass = (show) => 
{
    if(typeof(show) === "function"){
        return (show() ? "" : "hidden");
    }

    return (show ? "" : "hidden");
}
