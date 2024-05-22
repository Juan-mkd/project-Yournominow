document.getElementById("btnImprimir").addEventListener("click", function() {
    var doc = new jsPDF();
    doc.html(document.getElementById("contenido"), {
      callback: function(pdf) {
        pdf.save("constancia.pdf");
      }
    });
  });