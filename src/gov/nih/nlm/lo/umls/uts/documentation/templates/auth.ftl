        <style type="text/css">
            body {
                font-family: Arial;
            }

            
            #stUrl {
                width: 50%;
            }
            
            .formButton {
                background-color: #4CAF50;
                color: white;
                padding: 12px 20px;
                margin: 8px 0;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            
            ul.results {
            list-style-type:none;
            }
            
            ul.results li a {
            text-decoration:none;
            color: black;
            text-decoration: underline;
            }
            
            pre {
                white-space: pre-wrap;       /* Since CSS 2.1 */
                white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
                white-space: -pre-wrap;      /* Opera 4-6 */
                white-space: -o-pre-wrap;    /* Opera 7 */
                word-wrap: break-word;       /* Internet Explorer 5.5+ */
            }
            .error {
                color: red;
                font-weight:bold;
            }        
            
            input#apikey, input#service  {
            width: 400px;
            }
            
            .arrow {
            display: block;
            margin: auto;
            }
            
        </style>        
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script>
            $(document).ready(
                function() {
                $("#searchResults").hide();
                $("#tgtForm").submit(function (event) {
                    console.log("submitted");
                    $.post(
                        "https://utslogin.nlm.nih.gov/cas/v1/api-key", 
                        $("#tgtForm").serialize())
                    .done(function (data, status, jqXHR) {                            
                        console.log(data);
                        $('#tgtRes').text(data);
                        var tgtPattern = RegExp(/action=\"(http.*)\" method.*/g);
                        var tgt = tgtPattern.exec(data);
                        if(tgt) {
                            $("#tgtVal").text(tgt[1]);                            
                            $("#stUrl").text(tgt[1]);
                            $("#stUrlLabel").text(tgt[1]);                            
                        }

                    }).fail(function (error) {
                        console.log("Error - " + error);
                    });
                    event.preventDefault();
                });  

                $("#clearTgt").click(function() {
                    console.log("Clear called");
                    $("#tgtRes").text('');
                    $("#tgtVal").text('');
                    $("#stUrl").text('');
                    $("#stUrlLabel").text('');
                    $("#stVal").text('');
                    $("#searchResults").hide();
                });

                $("#stForm").submit(function(event) {
                    console.log("submitted");
                    var tgtUrl = $("#tgtVal").text();
                    $("#stUrlLabel").text(tgtUrl);
                    $.post(
                        tgtUrl, 
                        $("#stForm").serialize())
                    .done(function (data, status, jqXHR) {                            
                        console.log(data);
                        $('#stVal').text(data);
                    }).fail(function (error) {
                        console.log("Error - " + error);
                    });
                    event.preventDefault();
                });

                $("#clearSt").click(function() {
                    $("#stUrl").text('');
                    $("#stUrlLabel").text('');
                    $("#stVal").text('');
                });                

                $("#apiForm").submit(function(event) {
                    console.log("submitted");
                    var searchStr = $("#searchStr").val();                    
                    var ticket = $("#stVal").text();
                    $.get(
                        "https://uts-ws.nlm.nih.gov/rest/search/current?ticket="+ticket+"&string="+searchStr)
                    .done(function (data, status, jqXHR) {                            
                        console.log(data);
                        //var jsonStr = $("pre").text();
                        //var jsonObj = JSON.parse(data);
                        var jsonPretty = JSON.stringify(data, null, '\t');
                        $('#results').text(jsonPretty);
                        $("#searchResults").show();
                    }).fail(function (error) {
                        console.log("Error - " + error);
                    });
                    event.preventDefault();
                });

                $("#resetSearch").click(function() {
                    $("#results").text('');
                });                

            });
        
        </script>  