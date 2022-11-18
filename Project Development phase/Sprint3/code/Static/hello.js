anychart.onDocumentReady(function() {
        console.log("hello world")
        // set the data
        var data = {
            header: ["Name", "Available"],
            rows: [
              ["A +ve", 2],
              ["A -ve", 3],
              ["B +ve", 8],
              ["B -ve", 0],
              ["AB +ve", 10],
              ["AB -ve", 1],
              ["O +ve", 25],
              ["O -ve", 2]
        ]};

        // create the chart
        var chart = anychart.column();

        // add the data
        chart.data(data);

        // set the chart title
        chart.title("Plasma Donation Stats");

        // draw
        chart.container("chart");
        chart.draw();
      });
