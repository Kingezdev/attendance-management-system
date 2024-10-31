// Array to store marked attendance entries
const markedAttendance = [];

function markAttendance() {
  const rollNumber = document.getElementById('rollNumber').value;
  const studentName = document.getElementById('studentName').value;
  const date = document.getElementById('date').value;

  // Check which fields are missing and show the respective alert messages
  if (!rollNumber && !studentName && !date) {
    alert('Please enter Roll Number, Name, and Date before marking attendance.');
  } else if (!rollNumber && !studentName) {
    alert('Please enter Roll Number and Name before marking attendance.');
  } else if (!rollNumber && !date) {
    alert('Please enter Roll Number and Date before marking attendance.');
  } else if (!studentName && !date) {
    alert('Please enter Name and Date before marking attendance.');
  } else if (!rollNumber) {
    alert('Please enter Roll Number before marking attendance.');
  } else if (!studentName) {
    alert('Please enter Name before marking attendance.');
  } else if (!date) {
    alert('Please enter Date before marking attendance.');
  } else {
    // Check if the student has already marked attendance for the given date
    const hasMarkedAttendance = markedAttendance.some(entry => entry.rollNumber === rollNumber && entry.date === date);

    if (!hasMarkedAttendance) {
      // Add the new attendance entry to the array
      markedAttendance.push({ rollNumber, studentName, date });

      // Display the marked attendance entries in a table
      displayAttendanceList();
      
      // You can send this data to a server for storage and further processing
      // For now, we are just displaying it on the frontend
    } else {
      alert('Attendance already marked for this student on the specified date.');
    }
  }
}

function displayAttendanceList() {
  const resultContainer = document.getElementById('attendanceList');
  resultContainer.innerHTML = '';

  // Create a table
  const table = document.createElement('table');
  table.border = '1';
  table.bgColor = '#f38df7'
  table.cellPadding = '10px'
  table.cellSpacing = '5px'

  // Create the table header
  const headerRow = table.insertRow();
  const headerRollNumber = headerRow.insertCell(0);
  const headerName = headerRow.insertCell(1);
  const headerDate = headerRow.insertCell(2);

  headerRollNumber.textContent = 'Roll Number';
  headerName.textContent = 'Name';
  headerDate.textContent = 'Date';

  // Add data to the table
  markedAttendance.forEach(entry => {
    const row = table.insertRow();
    const cellRollNumber = row.insertCell(0);
    const cellName = row.insertCell(1);
    const cellDate = row.insertCell(2);

    cellRollNumber.textContent = entry.rollNumber;
    cellName.textContent = entry.studentName;
    cellDate.textContent = entry.date;
  });

  // Append the table to the result container
  resultContainer.appendChild(table);
}

function checkAttendance() {
  const startDate = document.getElementById('startDate').value;
  const endDate = document.getElementById('endDate').value;

  if (startDate && endDate) {
    // Filter attendance entries based on the specified date range
    const filteredAttendance = markedAttendance.filter(entry => entry.date >= startDate && entry.date <= endDate);

    // Display the filtered attendance entries in a table
    displayCheckResult(filteredAttendance);
  } else {
    alert('Please select both start and end dates.');
  }
}

function displayCheckResult(attendanceData) {
  const resultContainer = document.getElementById('checkResult');
  resultContainer.innerHTML = '';

  // Create a table
  const table = document.createElement('table');
  table.border = '1';
  table.bgColor = '#f38df7'
  table.cellPadding = '10px'
  table.cellSpacing = '5px'

  // Create the table header
  const headerRow = table.insertRow();
  const headerRollNumber = headerRow.insertCell(0);
  const headerName = headerRow.insertCell(1);
  const headerDate = headerRow.insertCell(2);

  headerRollNumber.textContent = 'Roll Number';
  headerName.textContent = 'Name';
  headerDate.textContent = 'Date';

  // Add data to the table
  attendanceData.forEach(entry => {
    const row = table.insertRow();
    const cellRollNumber = row.insertCell(0);
    const cellName = row.insertCell(1);
    const cellDate = row.insertCell(2);

    cellRollNumber.textContent = entry.rollNumber;
    cellName.textContent = entry.studentName;
    cellDate.textContent = entry.date;
  });

  // Append the table to the result container
  resultContainer.appendChild(table);
}
