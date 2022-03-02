// Saves options to chrome.storage


function save_options() {
  var mushtype = document.getElementById('mushtype').value;
  var trigger = document.getElementById('trigger').value;
  var threshold = document.getElementById('threshold').value;
  chrome.storage.sync.set({
    mushType: mushtype,
    triggerButton: trigger,
    threshold: threshold
  }, function() {
    // Update status to let user know options were saved.
    var status = document.getElementById('status');
    status.textContent = 'Options saved.';
    setTimeout(function() {
      status.textContent = '';
    }, 750);
  });
}


// stored in chrome.storage.
function restore_options() {
    chrome.storage.sync.get({
        mushType: 'loud',
        triggerButton: 'F20',
        threshold: 0.4
    }, function(items) {
        document.getElementById('mushtype').value = items.mushType;
        document.getElementById('trigger').value = items.triggerButton;
        document.getElementById('threshold').value = items.threshold;
    })
}

document.addEventListener('DOMContentLoaded', restore_options);
document.getElementById('mushtype').addEventListener('change', save_options);
document.getElementById('trigger').addEventListener('change', save_options);
document.getElementById('threshold').addEventListener('change', save_options);
document.getElementById('save').addEventListener('click', save_options);