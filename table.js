function create_sample_table(parentNode, head, body, foot, data) {
    if (typeof head == "undefined") {head = true;}
    if (typeof body == "undefined") {body = true;}
    if (typeof foot == "undefined") {foot = true;}
    //window.alert("here")
    $.get("/ragaslist",
    function (data) {
        if (!data) {
        data = {
            "head": [ "Ohho", "Author", "Publishing Date" ],
            "body": [
                [ "On Becoming a Person: A Therapist's View of Psychotherapy",  "Carl Rogers",                      "September 7, 1995"     ],
                [ "Anna Freud: A Biography",                                    "Elisabeth Young-Bruehl",           "July, 1994"            ],
            ],
            "foot": [ "Title", "Author", "Publishing Date" ],
        };}
       // window.alert(data.head + data.body + data.foot)
        var table = document.createElement("table");
        table.setAttribute("class","table is-bordered is-striped is-narrow is-hoverable is-fullwidth");
        table.id ="table1";
        var tr, th, td;
        // header
        tr = document.createElement("tr");
        var headers = data.head || [];
        for (var i=0;i<headers.length;i++) {
            th = document.createElement("th");
            th.innerHTML = headers[i];
            tr.appendChild(th);
        }
        if (head) {
            var thead = document.createElement("thead");
            thead.appendChild(tr);
            table.appendChild(thead);
        } else {
            table.appendChild(tr);
        }
        // end header

        // body
        var table_body = data.body || [];
       // window.alert(table_body)
       // window.alert(table_body[0].length)
        if (body) {
            var tbody = document.createElement("tbody");
        }
        for (var i=0;i<table_body.length;i++) {
            tr = document.createElement("tr");
            for (var j=0;j<table_body[i].length;j++) {
                td = document.createElement("td");
                td.innerHTML = table_body[i][j];
                tr.appendChild(td);
            }
            if (body) {
                tbody.appendChild(tr);
            } else {
                table.appendChild(tr);
            }
        }
        if (body) {
            table.appendChild(tbody);
        }
        // end body

        // footer
        if (foot) {
            var tfoot = document.createElement("tfoot");
            tr = document.createElement("tr");
            var footer = data.foot || [];
            for (var i=0;i<footer.length;i++) {
                th = document.createElement("th");
                th.innerHTML = footer[i];
                tr.appendChild(th);
            }
            tfoot.appendChild(tr);
            table.appendChild(tfoot);
        }
        // end footer

        if (parentNode) {
            parentNode.appendChild(table);
        }
    //return table;
    },"json");
}


