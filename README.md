# navidrome-uploader

Small Flask app that uploads audio files to a Navidrome music folder.

## Debian packaging

Debian packaging files are in `debian/`.

The package installs:
- app code in `/opt/navidrome-uploader`
- environment file in `/etc/default/navidrome-uploader/.env`
- systemd unit in `/lib/systemd/system/navidrome-uploader.service`
- Python dependencies in `/opt/navidrome-uploader/venv` during `postinst`

### Build a `.deb`

```sh
./release/build-deb.sh
```

The resulting package is written to the parent directory of the project.

