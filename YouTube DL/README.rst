==========
YouTube DL
==========

`Project Tracking`_

Utilizes `rg3/youtube-dl`_ for the audio/video downloading from a long list of `supported sites`_.

  Note: Post processing currently not supported.
  
:code:`On My iPhone/Local Storage/Downloads` will need to be added to Pythonista under External Files.


Setup
-----
Install StaSH using these in
https://github.com/ywangd/stash/blob/master/README.md#Installation


Running the shortcut while a download is still in progress will queue up the new video to download once the current one completes. Multiple downloads can be queued up like this. 


Known Issues
------------
- The current app will freeze up and crash after the Shortcut is run if started from the sharesheet. 
- The Shortcut hangs before audio/video selection if run from widget. 

.. _rg3/youtube-dl: https://github.com/rg3/youtube-dl 
.. _supported sites: https://github.com/rg3/youtube-dl/blob/master/docs/supportedsites.md
.. _Project Tracking: https://github.com/Harwood/Shortcuts/projects/1
