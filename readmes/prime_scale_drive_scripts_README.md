# Prime Scale App – Mobile Backup & Restore Scripts

These bash scripts let you safely **backup and restore** your Prime Scale App project directory to and from Google Drive using `rclone`. Works entirely on Android via Termux.

---

## 1. Backup Script

**File:** `backup_to_drive.sh`

```bash
#!/data/data/com.termux/files/usr/bin/bash

PROJECT_DIR="/storage/emulated/0/Documents/prime-scale-app"
REMOTE_NAME="gdrive"
REMOTE_PATH="prime-scale-backup"

rclone sync "$PROJECT_DIR" "$REMOTE_NAME:$REMOTE_PATH" --progress --delete-during

echo "✔ Backup complete: $PROJECT_DIR → $REMOTE_NAME:$REMOTE_PATH"
```

---

## 2. Restore Script

**File:** `restore_from_drive.sh`

```bash
#!/data/data/com.termux/files/usr/bin/bash

PROJECT_DIR="/storage/emulated/0/Documents/prime-scale-app"
REMOTE_NAME="gdrive"
REMOTE_PATH="prime-scale-backup"

rclone sync "$REMOTE_NAME:$REMOTE_PATH" "$PROJECT_DIR" --progress --delete-during

echo "✔ Restore complete: $REMOTE_NAME:$REMOTE_PATH → $PROJECT_DIR"
```

---

## How to Use

Make each script executable:
```bash
chmod +x backup_to_drive.sh
chmod +x restore_from_drive.sh
```

Run backup:
```bash
./backup_to_drive.sh
```

Run restore:
```bash
./restore_from_drive.sh
```

Ensure you have `rclone` installed and configured with a remote named `gdrive`.
