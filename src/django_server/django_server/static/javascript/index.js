$(document).ready(function() {

    /* For resizing form input boxes height */
    $('.resizeForm').on('keydown input', function() {
        this.style.removeProperty('height');
        this.style.height = (this.scrollHeight+2) + 'px';
    }).on('mousedown focus', function() {
        this.style.removeProperty('height');
        this.style.height = (this.scrollHeight+2) + 'px';
    });

});

function labelled_table(seq, lab) {
    const string_seq = seq;
    const string_label = lab;
    // Table will have 60 characters along each row
    const chunks = string_seq.match(/.{1,60}/g);
    const table = document.createElement("table");
    table.setAttribute('class', 'graph-wrapper');
    table.setAttribute('id', 'prediction');
    // label indexer for separate label list as zipping the sequence and label together in a tuple is tricky to work with.
    label_indexer = 0;
    chunks.forEach(chunk => {
        const row = document.createElement("tr");
        for (let i = 0; i < chunk.length; i++) {
            cell = document.createElement("td");
            // chunk[i] is an amino acid identifier
            cell.textContent = chunk[i]
            // Identify if amino acid is labelled ordered/disordered
            if (string_label[label_indexer] == '0') {
                cell.setAttribute('class', 'ordered');
            } else {
                cell.setAttribute('class', 'disordered');
            }
            row.appendChild(cell);
            label_indexer = label_indexer + 1;
        }
        table.appendChild(row);
    });

    document.body.appendChild(table);

    return table;
}

function downloadTableAsImage(seq_id) {
    // Get prediction table
    const table = document.querySelector('#prediction');
  
    // Use html2canvas to create a canvas from the table
    html2canvas(table).then(canvas => {
        // Convert the canvas to a PNG image
        const png_image = canvas.toDataURL('image/png');
    
        // Link for download button
        const download_button_link = document.createElement('a');
        download_button_link.href = png_image;
        download_button_link.download = seq_id.concat('-prediction.png');

        // Download link added to DOM
        document.body.appendChild(download_button_link);
        download_button_link.click();
    });
  }

