import streamlit as st
import streamlit.components.v1 as components


components.html(
"""<title>Organigrama MDHYHGC</title>
<script src="https://unpkg.com/gojs/release/go.js"></script>
</head>
<body>
  <div id="myDiagramDiv" style="width:100%; height:600px;"></div>

  <script>
    // Crear el diagrama
    var $ = go.GraphObject.make;
    var myDiagram = $(go.Diagram, "myDiagramDiv", {
      layout: $(go.TreeLayout, { angle: 90, layerSpacing: 35 })
    });

    // Definir los nodos y enlaces del organigrama
    myDiagram.nodeTemplate =
      $(go.Node, "Auto",
        $(go.Shape, "RoundedRectangle", { fill: "lightblue" }),
        $(go.Panel, "Vertical",
          $(go.TextBlock,
            { margin: 4, font:"italic 14px sans-serif" },
            new go.Binding("text", "title")),
          $(go.TextBlock,
            { margin: 4, font: "italic 14px sans-serif" },
            new go.Binding("text", "name")),
          $(go.TextBlock,
            { margin: 4, font: "italic 14px sans-serif" },
            new go.Binding("text", "CUIL", CUIL => "CUIL: " + CUIL)),
          $(go.TextBlock,
            { margin: 4, font: "italic 10px sans-serif" },
            new go.Binding("text", "code")),
          $(go.TextBlock,
            { margin: 4, font: "italic 10px sans-serif" },
            new go.Binding("text", "vigencia")),
          $(go.TextBlock,
            { margin: 4, font: "italic 10px sans-serif" },
            new go.Binding("text", "actoadm")),
          $(go.TextBlock,
            { margin: 4, font: "italic 10px sans-serif" },
            new go.Binding("text", "mailof",mailof => "Of: " + mailof)),
          $(go.TextBlock,
            { margin: 4, font: "italic 10px sans-serif" },
            new go.Binding("text", "mailalt", mailalt => "Alt: " + mailalt)),
          $(go.TextBlock,
            { margin: 4, font: "italic 10px sans-serif" },
            new go.Binding("text","telefono", telefono => "Tel: " + telefono)),
        )
      );

    myDiagram.linkTemplate =
      $(go.Link,
        $(go.Shape, { stroke: "black" })
      );

    // Definir los datos del organigrama
    var nodeDataArray = [
      { key: 0, name: "Maria Migliore", title: "Ministerio", CUIL: "27319252466", code: "45010000-MDHYHGC", vigencia:"10/12/19 - 1/1/4000", actoadm:"DEC/458/AJG/2019", mailof: "mmigliore@buenosaires.gob.ar",mailalt: "migliore.maria@gmail.com", telefono: "1128851168", parent: -1 },
      { key: 1, name: "", title: "Coordinación de Desarrollo Humano y Hábitat", code: "45010001 - CDHH", parent: 0 },
      { key: 2, name: "Giraudo, Mauricio Jesus", title: "SS Fortalecimiento Personal, Familiar y Comunitario", code: "45340000-SSFPFC", parent: 0 },
      { key: 3, name: "Martinez, Hebe", title: "Unidad de Auditoría Interna MDHYHGC", code: "45010020-UAIMDHYH", parent: 0 },
      // Agrega más nodos para los empleados adicionales...
    ];

    // Definir los enlaces del organigrama
    var linkDataArray = [
      { from: 0, to: 1 },
      { from: 0, to: 2 },
      { from: 0, to: 3 },
      // Agrega más enlaces entre los nodos...
    ];

    // Asignar los datos al diagrama
    myDiagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);

  </script>""", width=800, height=600, scrolling=True)