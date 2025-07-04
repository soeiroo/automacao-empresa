const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { exec } = require('child_process');
require('electron-reload')(__dirname);

function createWindow() {
  const win = new BrowserWindow({
    width: 900,
    height: 700,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
    icon: path.join(__dirname, 'web', 'favicon.ico'),
  });
  win.setMenuBarVisibility(false);
  win.loadFile(path.join(__dirname, 'web', 'index.html'));
  win.webContents.openDevTools(); // Adicionado para facilitar debug
}

// IPC para ping
ipcMain.handle('ping-pdv', async (event, ip) => {
  return new Promise((resolve) => {
    exec(`ping -n 1 -w 500 ${ip}`, (error, stdout, stderr) => {
      resolve(!error);
    });
  });
});

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
