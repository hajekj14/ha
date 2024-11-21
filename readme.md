enable i2c

1) remove the sd card from the pi and plug it into a pc running Linux
2) most likely linux will not mount the partition "hassos-boot" because it is FAT
	a) open a terminal window
	b) type > blkid
	c) in the resulting output, you'll see "LABEL="hassos-boot", note the location, mine is /dev/mmcblk0p1
	d) type > sudo mkdir /mnt/msdos
	e) type > sudo mount -t vfat /dev/mmcblk0p1 /mnt/msdos
	d) now you can open the file /mnt/msdos/config.txt
	e) uncomment the line "dtparam=i2c_arm=on"
3) If the hassos-overlay partition mounted, (if not, do step 2 for this partition)
	a) open the file: hassos-overlay\etc\modules-load.d\rpi-i2c.conf
	b) ensure it has only these 2 lines: (mine already did, likely from when trying "import usb" method)
		i2c-bcm2708
		i2c-dev
4) replace the sdcard back into the pi and start normally
	a) the i2c bus should be functioning now