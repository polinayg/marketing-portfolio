/* Reassemble unchanged source PDFs from small static parts. */
(async function () {
  'use strict';
  const params = new URLSearchParams(location.search);
  const documents = {
    'ak-before': 'assets/docs/pdf/ak-before/manifest.json',
    'ak-after': 'assets/docs/pdf/ak-after/manifest.json'
  };
  const status = document.getElementById('pdf-status');
  try {
    const path = documents[params.get('document')];
    if (!path) throw new Error('Choose a PDF from the website case study.');
    const manifestUrl = new URL(path, location.href);
    const response = await fetch(manifestUrl);
    if (!response.ok) throw new Error('The PDF could not be loaded. Please try again.');
    const manifest = await response.json();
    document.getElementById('pdf-title').textContent = manifest.label;
    document.title = manifest.label + ' | Original PDF';
    const parts = new Array(manifest.parts.length);
    let next = 0, complete = 0;
    async function worker() {
      while (next < parts.length) {
        const i = next++;
        const result = await fetch(new URL(manifest.parts[i], manifestUrl));
        if (!result.ok) throw new Error('The PDF could not be loaded. Please try again.');
        parts[i] = new Uint8Array(await result.arrayBuffer());
        complete++;
        status.textContent = 'Loading original PDF… ' + Math.round(complete / parts.length * 100) + '%';
      }
    }
    await Promise.all(Array.from({length: Math.min(6, parts.length)}, worker));
    const bytes = new Uint8Array(parts.reduce((n, part) => n + part.length, 0));
    let offset = 0;
    for (const part of parts) { bytes.set(part, offset); offset += part.length; }
    if (bytes.length !== manifest.size) throw new Error('The PDF download was incomplete. Please reload.');
    const digest = await crypto.subtle.digest('SHA-256', bytes);
    const hash = Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2, '0')).join('');
    if (hash !== manifest.sha256) throw new Error('The PDF download was incomplete. Please reload.');
    const url = URL.createObjectURL(new Blob([bytes], {type:'application/pdf'}));
    const open = document.getElementById('pdf-open');
    const download = document.getElementById('pdf-download');
    open.href = url; open.hidden = false;
    download.href = url; download.download = manifest.file_name; download.hidden = false;
    const frame = document.getElementById('pdf-frame');
    frame.src = url; frame.hidden = false;
    status.textContent = 'Original PDF ready. Open it to zoom, or download the unchanged file.';
    if (params.get('download') === '1') download.click();
  } catch (error) {
    status.textContent = error.message || 'The PDF could not be loaded. Please try again.';
  }
})();
