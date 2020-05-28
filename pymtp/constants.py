#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# PyMTP
# Developed by: Nick Devito (nick@nick125.com)
# (c) 2008 Nick Devito
# Released under the GPLv3 or later.
#

import ctypes

# Abstracted from libmtp 0.3.3's libmtp.h. This must be kept in sync.
#  last checked in version 1.1.17
LIBMTP_Filetype = {
    # 0 for LIBMTP_FILETYPE_FOLDER
	"WAV":					ctypes.c_int(1),
	"MP3":					ctypes.c_int(2),
	"WMA":					ctypes.c_int(3),
	"OGG":					ctypes.c_int(4),
	"AUDIBLE":				ctypes.c_int(5),
	"MP4":					ctypes.c_int(6),
	"UNDEF_AUDIO":				ctypes.c_int(7),
	"WMV":					ctypes.c_int(8),
	"AVI":					ctypes.c_int(9),
	"MPEG":					ctypes.c_int(10),
	"ASF":					ctypes.c_int(11),
	"QT":					ctypes.c_int(12),
	"UNDEF_VIDEO":				ctypes.c_int(13),
	"JPEG":					ctypes.c_int(14),
	"JFIF":					ctypes.c_int(15),
	"TIFF":					ctypes.c_int(16),
	"BMP":					ctypes.c_int(17),
	"GIF":					ctypes.c_int(18),
	"PICT":					ctypes.c_int(19),
	"PNG":					ctypes.c_int(20),
	"VCALENDAR1":				ctypes.c_int(21),
	"VCALENDAR2":				ctypes.c_int(22),
	"VCARD2":				ctypes.c_int(23),
	"VCARD3":				ctypes.c_int(24),
	"WINDOWSIMAGEFORMAT":			ctypes.c_int(25),
	"WINEXEC":				ctypes.c_int(26),
	"TEXT":					ctypes.c_int(27),
	"HTML":					ctypes.c_int(28),
	"FIRMWARE":				ctypes.c_int(29),
	"AAC":					ctypes.c_int(30),
	"MEDIACARD":				ctypes.c_int(31),
	"FLAC":					ctypes.c_int(32),
	"MP2":					ctypes.c_int(33),
	"M4A":					ctypes.c_int(34),
	"DOC":					ctypes.c_int(35),
	"XML":					ctypes.c_int(36),
	"XLS":					ctypes.c_int(37),
	"PPT":					ctypes.c_int(38),
	"MHT":					ctypes.c_int(39),
	"JP2":					ctypes.c_int(40),
	"JPX":					ctypes.c_int(41),
	"ALBUM":				ctypes.c_int(42),
	"PLAYLIST":				ctypes.c_int(43),
	"UNKNOWN":				ctypes.c_int(44),
	}
	
# Synced from libmtp's libmtp.h. Must be kept in sync.
#  first checked in version 0.2.6.1
#  last checked in version 1.1.6
LIBMTP_Error_Number = {
	"NONE":					ctypes.c_int(0),
	"GENERAL":				ctypes.c_int(1),
	"PTP_LAYER":				ctypes.c_int(2),
	"USB_LAYER":				ctypes.c_int(3),
	"MEMORY_ALLOCATION":			ctypes.c_int(4),
	"NO_DEVICE_ATTACHED":			ctypes.c_int(5),
	"STORAGE_FULL":				ctypes.c_int(6),
	"CONNECTING":				ctypes.c_int(7),
	"CANCELLED":				ctypes.c_int(8),
}
