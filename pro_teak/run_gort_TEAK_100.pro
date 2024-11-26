pro run_gort

 tek_color
  ; Setting plotting
  set_plot,'ps'
  
  ;device, file= 'comp.eps', /color,/TIMES,/BOLD,/portrait, ysize=28, YOFFSET=0, xsize=21, xOFFSET=0.0
  device, file= 'comp_TEAK_100.eps', /TIMES,/BOLD,/portrait, ysize=28, YOFFSET=0, xsize=21, xOFFSET=0.0
  !p.multi=[0,4,6]

nsite=3
indir='input/'
indir='/data/shared/src/STV/NEON_TEAK/allen/Gort_100/'
fplot = findfile(indir)

for i=1, 5 do begin

  cmd='cp '+indir+fplot(i-1)+ ' gort.in'
  spawn, cmd, result, err
  if (err ne '') then stop

  ; Run GORT model. For only 1 type on the site, it will run single gort. While for 2 types, it runs convolute GORT
  cmd='../model/gort_lidar > temp.txt'

  spawn, cmd, result, err
 ; if (err ne '') then stop
  print, 'output created'

  ;run guassian convolution
  temp_str=''
  gn_level=0
  gout = {height:0.0,fp:0.0,efp:0.0,pgap:0.0,dpdz:0.0,wvfm:0.0}

;read gort output file 
  close,2
  openr, 2, 'gort.out'
  readf, 2, gn_level,dz
  print, gn_level, dz
  n_ext=10./dz  
  n_tot=gn_level+n_ext

  ght=fltarr(n_tot)
  wvfm=fltarr(n_tot)
  gwvfm=wvfm
  ght(0:n_ext-1)=findgen(n_ext)*dz-10 ;extend height to below ground 10m deep 
  wvfm(0:n_ext-1)=0             ;extend wvfm to below ground 10m deep
  
  readf, 2, temp_str
  ;print, temp_str
  readf, 2, temp_str
  ;print, temp_str
  ;readf, 2, temp_str
  ;print, temp_str
  for ilevel=0, gn_level-1 do begin
;    print,ilevel
      readf, 2, gout
      ght[ilevel+n_ext]=gout.height
      wvfm[ilevel+n_ext]=gout.wvfm
  endfor
  close, 2

  width = fix(0.6/dz)+1 ;LVIS gaussian width=10ns(10ns*0.15m=1.5m)/2.35482=0.63m, witdth #=0.63/dz
  gwvfm=gsmooth(wvfm,width)
 
  jx1=0
  jx2=0.3
  jh1=-5
  jh2=40 
  cs =1.4
  ct =1.4
  if (i eq 1) then begin
      plot, gwvfm, ght,title=fplot(i-1),xtitle='Normalized WF', ytitle='Height(m)', xrange=[jx1,jx2], yrange=[jh1,jh2],charsize=cs,charthick=ct
  ;    /NODATA, linestyle = 0,thick=4, yrange=[jh1,jh2], xrange=[jx1,jx2],charsize=cs,charthick=ct

      endif else begin  
          plot, gwvfm, ght,title=fplot(i-1),xtitle='Normalized WF', ytitle='Height(m)', xrange=[jx1,jx2], yrange=[jh1,jh2],charsize=cs,charthick=ct
;           /NODATA, linestyle = 0,thick=4, yrange=[jh1,jh2],,charsize=2.2,charthick=ct
          endelse
 
;  save, filename='outputs/gort_wvfm'+strtrim(string(i), 2)+'.sav',ght,gwvfm
endfor
DEVICE,/CLOSE 

stop

end
