function sanitizeInput(msg){
    if (msg.includes("<script>") || msg.includes("</script>")){
        return "BAD INPUT";
        
    } else return msg;
}


app.get('/', (req, res) => {
    //if there's a query parameter called "poem" then we gotta make sure and clean it!
    if (req.query.poem && typeof(req.query.poem) == 'string'){
        let input = req.query.poem.toLowerCase();
        //Get rid of script tags. Now I'm protected against XSS! 
        let cleaned = sanitizeInput(input);
        res.send(template(cleaned, ""));
    } else {
        res.send(template("", ""));
    }
})