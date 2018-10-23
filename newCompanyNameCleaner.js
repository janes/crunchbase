var alasql = require("alasql");

alasql.promise('SELECT * FROM XLSX("/Users/justin/Downloads/HT Potentially Entrepreneurial RT Region Firms")').then(function(data){
    excelData = data;
    let compName = [];
    let i = 0;
    while (i < data.length) {
        compName[i] = data[i].company;
        i++;
    }
    i = 0;
    while (i < compName.length) {
        let k = compName[i].length - 1;
        let yet = false;
        while (k > 0) {
            if (compName[i].substring(compName[i].length - 2, compName[i].length - 1) === " " && !yet) {
                compName[i] = compName[i].substr(0, compName[i].length - 1);
            } 
            if (compName[i].substring(compName[i].length - 2, compName[i].length - 1) != " ") {
                yet = true;
            }
            k--;
        }
        i++;
    }
    i = 0;
    while (i < compName.length) {
        compName[i] = compName[i].substring(0, compName[i].length - 1)
        compName[i] = compName[i].toLowerCase();
        let length = compName[i].length;
        //console.log("substr:" + compName[i].substring(length - 3, length));
        if (compName[i].substring(length - 4, length) === " inc") {
            compName[i] = compName[i].substr(0, length - 4);
        }
        if (compName[i].substring(length - 4, length) === " llc") {
            compName[i] = compName[i].substr(0, length - 4);
        }
        if (compName[i].substring(length - 5, length) === " pllc") {
            compName[i] = compName[i].substr(0, length - 5);
        }
        if (compName[i].substring(length - 3, length) === " co") {
            compName[i] = compName[i].substr(0, length - 3);
        }
        i++;
    }
    console.log(compName);
    alasql('SELECT column INTO TXT("cleanedCompanyNames1.txt") FROM ?', [compName]);
});
