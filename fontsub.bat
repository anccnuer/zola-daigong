char.exe
hb-subset --output-file=./static/assets/Zhuque.ttf input.ttf --text-file=hanzi.txt --name-IDs=* --layout-features=* --no-hinting --drop-tables=DSIG,hdmx,VDMX,LTSH,PCLT,vhea,vmtx,VORG,gasp
fontconv ./static/assets/Zhuque.ttf ./static/assets/Zhuque.woff2
pause