// Ensure this is the correct path to your Python executable
const command = `"C:\\Users\\sohum\\OneDrive\\Documents\\SparkHacks2024\\dist\\retreive.exe"`;




// Retrieve data from Python side
exec(command, (error, stdout, stderr) => {
    if (error) {
        console.error(`exec error: ${error}`);
        return;
    }
    if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
    }
    // Check raw output
    console.log(`Raw output: ${stdout}`);
   
    // Attempt to parse JSON only if stdout is not empty
    if (stdout) {
        try {
            const data = JSON.parse(stdout);
            console.log('Parsed data:', data);
        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
        }
    } else {
        console.log('No output received.');
    }
});
