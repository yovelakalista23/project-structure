<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1oWls66ZouV9nqiLH9ldCNUYAvRMF1mr1#scrollTo=zIK2HSOQlXdB -->
<html lang="en" theme="adaptive" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script type="text/javascript" async="" charset="utf-8" src="./README_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-wxK1GRvr3VMaoMrFu9sAGWa5hCt0P7FJvlkPWu68jhr4d1K9FSq2WgMoHPsWQpHL" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./README_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-wxK1GRvr3VMaoMrFu9sAGWa5hCt0P7FJvlkPWu68jhr4d1K9FSq2WgMoHPsWQpHL" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./README_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-wxK1GRvr3VMaoMrFu9sAGWa5hCt0P7FJvlkPWu68jhr4d1K9FSq2WgMoHPsWQpHL" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./README_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-wxK1GRvr3VMaoMrFu9sAGWa5hCt0P7FJvlkPWu68jhr4d1K9FSq2WgMoHPsWQpHL" nonce=""></script><script src="./README_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./README_files/cb=gapi.loaded_0" nonce="" async=""></script><script type="text/javascript" async="" src="./README_files/js" nonce=""></script><script async="" src="./README_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>README.md - Colab</title><link href="./README_files/css2" rel="stylesheet"><link href="./README_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_3d:not(.gb_qe){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Qa:hover:after,a.gb_Qa:focus:after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua{background:#f8f8f8}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ua{cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_F{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_F:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_F:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_F:active,#gb .gb_Va.gb_F:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_cd{display:inline-block;vertical-align:middle}.gb_Pe .gb_Q{bottom:-3px;right:-5px}.gb_C{position:relative}.gb_A{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_A{cursor:pointer;text-decoration:none}.gb_A,a.gb_A{color:#000}.gb_dd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_ed{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_ed{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_cd.gb_Tc .gb_dd,.gb_cd.gb_Tc .gb_ed,.gb_cd.gb_Tc .gb_la,.gb_Tc.gb_la{display:block}.gb_cd.gb_Tc.gb_fd .gb_dd,.gb_cd.gb_Tc.gb_fd .gb_ed{display:none}.gb_Qe{position:absolute;right:8px;top:62px;z-index:-1}.gb_gd .gb_dd,.gb_gd .gb_ed,.gb_gd .gb_la{margin-top:-10px}.gb_cd:first-child,#gbsfw:first-child+.gb_cd{padding-left:4px}.gb_Fa.gb_Re .gb_cd:first-child{padding-left:0}.gb_Se{position:relative}.gb_2c .gb_Se,.gb_Jd .gb_Se{float:right}.gb_A{padding:8px;cursor:pointer}.gb_A:after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_hd:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_id button svg,.gb_A{-webkit-border-radius:50%;border-radius:50%}.gb_id button:focus:not(:focus-visible) svg,.gb_id button:hover svg,.gb_id button:active svg,.gb_A:focus:not(:focus-visible),.gb_A:hover,.gb_A:active,.gb_A[aria-expanded=true]{outline:none}.gb_Lc .gb_id.gb_jd button:focus-visible svg,.gb_id button:focus-visible svg,.gb_A:focus-visible{outline:1px solid #202124}.gb_Lc .gb_id button:focus-visible svg,.gb_Lc .gb_A:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Lc .gb_id.gb_jd button:focus-visible svg,.gb_id button:focus-visible svg,.gb_Lc .gb_id button:focus-visible svg{outline:1px solid currentcolor}}.gb_Lc .gb_id.gb_jd button:focus svg,.gb_Lc .gb_id.gb_jd button:focus:hover svg,.gb_id button:focus svg,.gb_id button:focus:hover svg,.gb_A:focus,.gb_A:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Lc .gb_id.gb_jd button:active svg,.gb_id button:active svg,.gb_A:active{background-color:rgba(60,64,67,.12)}.gb_Lc .gb_id.gb_jd button:hover svg,.gb_id button:hover svg,.gb_A:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_A.gb_Za:hover{background-color:transparent}.gb_A[aria-expanded=true],.gb_A:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_A[aria-expanded=true] .gb_E{fill:#5f6368;opacity:1}.gb_Lc .gb_id button:hover svg,.gb_Lc .gb_A:hover{background-color:rgba(232,234,237,.08)}.gb_Lc .gb_id button:focus svg,.gb_Lc .gb_id button:focus:hover svg,.gb_Lc .gb_A:focus,.gb_Lc .gb_A:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Lc .gb_id button:active svg,.gb_Lc .gb_A:active{background-color:rgba(232,234,237,.12)}.gb_Lc .gb_A[aria-expanded=true],.gb_Lc .gb_A:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Lc .gb_A[aria-expanded=true] .gb_E{fill:#fff;opacity:1}.gb_cd{padding:4px}.gb_Fa.gb_Re .gb_cd{padding:4px 2px}.gb_Fa.gb_Re .gb_y.gb_cd{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_kd{left:0;right:auto}@media (max-width:350px){.gb_la.gb_kd{left:0}}.gb_Te .gb_la{top:56px}.gb_R{display:none!important}.gb_nd{visibility:hidden}.gb_I .gb_A,.gb_ka .gb_I .gb_A{background-position:-64px -29px}.gb_1 .gb_I .gb_A{background-position:-29px -29px;opacity:1}.gb_I .gb_A,.gb_I .gb_A:hover,.gb_I .gb_A:focus{opacity:1}.gb_K{display:none}@media screen and (max-width:319px){.gb_ld:not(.gb_md) .gb_I{display:none;visibility:hidden}}.gb_Q{display:none}.gb_9c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_9c.gb_ad{color:#3c4043}.gb_Fa.gb_cc .gb_9c{margin-bottom:0}.gb_sd.gb_ud .gb_9c{padding-left:4px}.gb_Fa.gb_cc .gb_vd{position:relative;top:-2px}.gb_bd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Fa.gb_Sc{min-width:120px}.gb_Fa.gb_wd .gb_xd{display:none}.gb_Fa.gb_wd .gb_ld{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Dd{position:fixed;top:0;width:100%}.gb_yd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Ed{height:64px}.gb_ld{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_cc) .gb_ld{padding:8px}.gb_Fa.gb_Fd .gb_ld{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa .gb_ld.gb_md.gb_Hd{min-width:0}.gb_Fa.gb_cc .gb_ld{padding:4px;padding-left:8px;min-width:0}.gb_xd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Ad>.gb_xd{display:table-cell;width:100%}.gb_sd{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa.gb_cc .gb_sd{padding-right:14px}.gb_Bd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Bd>:only-child{display:inline-block}.gb_Cd.gb_3c{padding-left:4px}.gb_Cd.gb_Id,.gb_Fa.gb_Fd .gb_Cd,.gb_Fa.gb_cc:not(.gb_Jd) .gb_Cd{padding-left:0}.gb_Fa.gb_cc .gb_Cd.gb_Id{padding-right:0}.gb_Fa.gb_cc .gb_Cd.gb_Id .gb_Wa{margin-left:10px}.gb_3c{display:inline}.gb_Fa.gb_Wc .gb_Cd.gb_Kd,.gb_Fa.gb_Jd .gb_Cd.gb_Kd{padding-left:2px}.gb_9c{display:inline-block}.gb_Cd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Jd{height:48px}.gb_Fa.gb_Jd{min-width:auto}.gb_Jd .gb_Cd{float:right;padding-left:32px}.gb_Jd .gb_Cd.gb_Ld{padding-left:0}.gb_Md{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_pd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Nd{color:black}.gb_Lc{color:white}.gb_Fa a,.gb_Pc a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_Pc svg,.gb_sd .gb_td,.gb_2c .gb_td{color:#5f6368;opacity:1}.gb_Lc svg,.gb_Pc.gb_Uc svg,.gb_Lc .gb_sd .gb_td,.gb_Lc .gb_sd .gb_Kc,.gb_Lc .gb_sd .gb_vd,.gb_Pc.gb_Uc .gb_td{color:rgba(255,255,255,.87)}.gb_Lc .gb_sd .gb_Od:not(.gb_Pd){opacity:.87}.gb_ad{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Lc .gb_ad,.gb_Nd .gb_ad{opacity:1}.gb_Qd{position:relative}.gb_L{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_Lc a.gb_X,.gb_Lc span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_qd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Jd .gb_qd{margin-left:8px}#gb a.gb_Ua.gb_qd{cursor:pointer}.gb_Ua.gb_qd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_qd:focus,.gb_Ua.gb_qd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_qd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_qd{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_cc .gb_qd{padding:9px 15px;min-width:80px}.gb_Rd{text-align:left}#gb .gb_Lc a.gb_qd:not(.gb_F),#gb.gb_Lc a.gb_qd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_F.gb_qd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Lc a.gb_qd:hover:not(.gb_F),#gb.gb_Lc a.gb_qd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_F.gb_qd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Lc a.gb_qd:focus:not(.gb_F),#gb .gb_Lc a.gb_qd:focus:hover:not(.gb_F),#gb.gb_Lc a.gb_qd:focus:not(.gb_F),#gb.gb_Lc a.gb_qd:focus:hover:not(.gb_F){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_F.gb_qd:focus,#gb a.gb_Ua.gb_F.gb_qd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Lc a.gb_qd:active:not(.gb_F),#gb.gb_Lc a.gb_qd:active{background:#ecf3fe}#gb a.gb_Ua.gb_F.gb_qd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_J{display:none}@media screen and (max-width:319px){.gb_ld .gb_I{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_F{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_F .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_F:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_F:focus-visible,.gb_Wa.gb_F:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_F:active,.gb_Wa.gb_Tc.gb_F:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_F .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Ic{vertical-align:middle}.gb_Fa:not(.gb_cc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_Sd{max-height:32px;width:78px}.gb_Wa.gb_F .gb_Sd{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_eb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_eb.gb_P{height:30px;width:30px}.gb_eb.gb_P:hover,.gb_eb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_fb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_wc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_gb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_gb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_hb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_A.gb_hb{width:auto}.gb_hb:hover,.gb_hb:focus{opacity:.85}.gb_gd .gb_hb,.gb_gd .gb_Vd{line-height:26px}#gb#gb.gb_gd a.gb_hb,.gb_gd .gb_Vd{font-size:11px;height:auto}.gb_ib{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_ib{opacity:.85}.gb_Wa>.gb_y{padding:3px 3px 3px 4px}.gb_Wd.gb_nd{color:#fff}.gb_1 .gb_hb,.gb_1 .gb_ib{opacity:1}#gb#gb.gb_1.gb_1 a.gb_hb,#gb#gb .gb_1.gb_1 a.gb_hb{color:#fff}.gb_1.gb_1 .gb_ib{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Xd .gb_y,.gb_Zd .gb_y{position:absolute;right:1px}.gb_y.gb_0,.gb_jb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_0d.gb_1d .gb_hb{width:30px!important}.gb_2d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_3d .gb_2d,.gb_4d .gb_2d{right:0;top:0}.gb_y .gb_A{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.RRlsmNlDmQQ.2019.O","co.id","en-GB","425",0,[4,2,"","","","677578146","0"],null,"D4r0Zs_NHcq5p84Pv-LzqQ0",null,0,"og.qtm.pZbbn6aKAZ8.L.W.O","AA2YrTv3Qzh6Ja6eSLzWU_FOQIMZM5uKUQ","AA2YrTt6If9d1pi4yP4MpRCU4A1M3rvNtg","",2,1,200,"IDN",null,null,"425","425",1,null,null,114591953,1,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","yovelakalista23@gmail.com","","AOAJtj0eTAVzEhHzXnHrfHV-B-vlBnJMpU7AG9Ntu802q8eE2uDHQILxw-3DhbTBa4cVewCSfBjui5ylYlTHt8nufAMnPh6zqQ",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en-GB"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.SpvAvsXfWWo.O/am=AACA/d=1/rs=AHpOoo-MoqWi0fF1M09Ccs-6QfulXvxfdg/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20240903.0_p1","en-GB",null,0],[0.009999999776482582,"co.id","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IDN","en-GB","677578146.0",8,null,1,0,null,null,null,null,"3700949,3701322",null,null,null,"D4r0Zs_NHcq5p84Pv-LzqQ0",0,0,0,null,2,5,"nn",23,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.RRlsmNlDmQQ.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTv3Qzh6Ja6eSLzWU_FOQIMZM5uKUQ"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.pZbbn6aKAZ8.L.W.O/m=qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTt6If9d1pi4yP4MpRCU4A1M3rvNtg"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026galu=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",0],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en-GB",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026timeStmp=1727302159\u0026secTok=.AG5fkS9jKzpPUBwKjfFXoKp7Tc06xdD_gQ\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,0,1,0,0,0,0],0,null,null,null,0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ca,ja,ka,oa,qa,ra,Aa,Ba,Da,Ea,Fa,Ia,Na,Za,Ya,eb,gb,fb,hb,ib,nb,ob,sb,vb,pb,ub,tb,rb,qb,wb,xb,Eb,Hb,Ib,Jb,Kb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.rj=!0;return a};ca=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};
_.ea=function(a){_.t.setTimeout(()=>{throw a;},0)};_.fa=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};ja=function(a){return ha?ia?ia.brands.some(({brand:b})=>b&&b.indexOf(a)!=-1):!1:!1};_.u=function(a){return _.fa().indexOf(a)!=-1};ka=function(){return ha?!!ia&&ia.brands.length>0:!1};_.la=function(){return ka()?!1:_.u("Opera")};_.ma=function(){return ka()?!1:_.u("Trident")||_.u("MSIE")};_.na=function(){return _.u("Firefox")||_.u("FxiOS")};
_.pa=function(){return _.u("Safari")&&!(oa()||(ka()?0:_.u("Coast"))||_.la()||(ka()?0:_.u("Edge"))||(ka()?ja("Microsoft Edge"):_.u("Edg/"))||(ka()?ja("Opera"):_.u("OPR"))||_.na()||_.u("Silk")||_.u("Android"))};oa=function(){return ka()?ja("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(ka()?0:_.u("Edge"))||_.u("Silk")};qa=function(){return ha?!!ia&&!!ia.platform:!1};ra=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.sa=function(){return ra()||_.u("iPad")||_.u("iPod")};
_.ta=function(){return qa()?ia.platform==="macOS":_.u("Macintosh")};_.va=function(a,b){return _.ua(a,b)>=0};_.wa=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.xa=function(a){return a!=null&&a instanceof Uint8Array};_.ya=function(a){return Array.prototype.slice.call(a)};_.za=function(a){return!!((a[_.v]|0)&2)};Aa=function(a,b){b[_.v]=(a|0)&-14591};
Ba=function(a,b){b[_.v]=(a|34)&-14557};Da=function(a){return!(!a||typeof a!=="object"||a.i!==Ca)};Ea=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};Fa=function(a){return!Array.isArray(a)||a.length?!1:(a[_.v]|0)&1?!0:!1};_.Ga=function(a){if(a&2)throw Error();};Ia=function(a,b){(b=_.Ha?b[_.Ha]:void 0)&&(a[_.Ha]=_.ya(b))};_.Ka=function(){const a=Error();Ja(a,"incident");_.ea(a)};_.La=function(a){a=Error(a);Ja(a,"warning");return a};
_.Ma=function(a,b){if(a.length!==b.length)return!1;for(const e in b){var c=Number(e),d;if(d=Number.isInteger(c))d=a[c],c=b[c],d=!(Number.isNaN(d)?Number.isNaN(c):d===c);if(d)return!1}return!0};Na=function(){_.Ka()};_.Pa=function(a,b){let c,d;return(c=_.Oa)==null?void 0:(d=c.get(b))==null?void 0:d.get(a)};_.Ra=function(a){if(typeof a!=="boolean")throw Error("s`"+_.Qa(a)+"`"+a);return a};_.Sa=function(a){if(!Number.isFinite(a))throw _.La("enum");return a|0};
_.Ta=function(a){if(typeof a!=="number")throw _.La("int32");if(!Number.isFinite(a))throw _.La("int32");return a|0};_.Ua=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Va=function(a){return a==null||typeof a==="string"?a:void 0};_.Xa=function(a,b,c){if(a!=null&&typeof a==="object"&&a.Dd===_.Wa)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&(a[_.v]=e);return new b(a)}};Za=function(a,b){return Ya(b)};
Ya=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "bigint":return(0,_.$a)(a)?Number(a):String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(Fa(a))return}else{if(_.xa(a))return _.wa(a);if("function"==typeof _.ab&&a instanceof _.ab)return a.hg()}}return a};_.cb=function(a,b){bb=b;a=new a(b);bb=void 0;return a};
_.db=function(a,b,c){a==null&&(a=bb);bb=void 0;if(a==null){var d=96;c?(a=[c],d|=512):a=[];b&&(d=d&-33521665|(b&1023)<<15)}else{if(!Array.isArray(a))throw Error("t");d=a[_.v]|0;if(d&2048)throw Error("w");if(d&64)return a;d|=64;if(c&&(d|=512,c!==a[0]))throw Error("x");a:{c=a;const e=c.length;if(e){const f=e-1;if(Ea(c[f])){d|=256;b=f-(+!!(d&512)-1);if(b>=1024)throw Error("y");d=d&-33521665|(b&1023)<<15;break a}}if(b){b=Math.max(b,e-(+!!(d&512)-1));if(b>1024)throw Error("z");d=d&-33521665|(b&1023)<<15}}}a[_.v]=
d;return a};eb=function(a,b,c){const d=_.ya(a);var e=d.length;const f=b&256?d[e-1]:void 0;e+=f?-1:0;for(b=b&512?1:0;b<e;b++)d[b]=c(d[b]);if(f){b=d[b]={};for(const g in f)b[g]=c(f[g])}Ia(d,a);return d};gb=function(a,b,c,d,e){if(a!=null){if(Array.isArray(a))a=Fa(a)?void 0:e&&(a[_.v]|0)&2?a:fb(a,b,c,d!==void 0,e);else if(Ea(a)){const f={};for(let g in a)f[g]=gb(a[g],b,c,d,e);a=f}else a=b(a,d);return a}};
fb=function(a,b,c,d,e){const f=d||c?a[_.v]|0:0;d=d?!!(f&32):void 0;const g=_.ya(a);for(let h=0;h<g.length;h++)g[h]=gb(g[h],b,c,d,e);c&&(Ia(g,a),c(f,g));return g};hb=function(a){return a.Dd===_.Wa?a.toJSON():Ya(a)};
ib=function(a,b,c=Ba){if(a!=null){if(a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=a[_.v]|0;if(d&2)return a;b&&(b=d===0||!!(d&32)&&!(d&64||!(d&16)));return b?(a[_.v]=(d|34)&-12293,a):fb(a,ib,d&4?Ba:c,!0,!0)}a.Dd===_.Wa&&(c=a.ha,d=c[_.v],a=d&2?a:_.jb(a,c,d,!0));return a}};_.jb=function(a,b,c,d){_.kb(a);return _.cb(a.constructor,_.lb(b,c,d))};_.lb=function(a,b,c){const d=c||b&2?Ba:Aa,e=!!(b&32);a=eb(a,b,f=>ib(f,e,d));a[_.v]=a[_.v]|32|(c?2:0);return a};
_.mb=function(a){const b=a.ha,c=b[_.v];return c&2?_.jb(a,b,c,!1):a};nb=function(a){return a};ob=function(a){return a};sb=function(a,b,c,d){return pb(a,b,c,d,qb,rb)};vb=function(a,b,c,d){return pb(a,b,c,d,tb,ub)};
pb=function(a,b,c,d,e,f){if(!c.length&&!d)return 0;var g=0;let h=0,k=0;var l=0;let m=0;for(var p=c.length-1;p>=0;p--){var r=c[p];d&&p===c.length-1&&r===d||(l++,r!=null&&k++)}if(d)for(var q in d)p=+q,isNaN(p)||(m+=wb(p),h++,p>g&&(g=p));l=e(l,k)+f(h,g,m);q=k;p=h;r=g;let w=m;for(let D=c.length-1;D>=0;D--){var C=c[D];if(C==null||d&&D===c.length-1&&C===d)continue;C=D-b;const H=e(C,q)+f(p,r,w);H<l&&(a=1+C,l=H);p++;q--;w+=wb(C);r=Math.max(r,C)}b=e(0,0)+f(p,r,w);b<l&&(a=0,l=b);if(d){p=h;r=g;w=m;q=k;for(const D in d)d=
+D,isNaN(d)||d>=1024||(p--,q++,w-=D.length,g=e(d,q)+f(p,r,w),g<l&&(a=1+d,l=g))}return a};ub=function(a,b,c){return c+a*3+(a>1?a-1:0)};tb=function(a,b){return(a>1?a-1:0)+(a-b)*4};rb=function(a,b){return a==0?0:9*Math.max(1<<32-Math.clz32(a+a/2-1),4)<=b?a==0?0:a<4?100+(a-1)*16:a<6?148+(a-4)*16:a<12?244+(a-6)*16:a<22?436+(a-12)*19:a<44?820+(a-22)*17:52+32*a:40+4*b};qb=function(a){return 40+4*a};wb=function(a){return a>=100?a>=1E4?Math.ceil(Math.log10(1+a)):a<1E3?3:4:a<10?1:2};
xb=function(a,b,c,d){b=d+(+!!(b&512)-1);if(!(b<0||b>=a.length||b>=c))return a[b]};_.yb=function(a,b,c,d){const e=b>>15&1023||536870912;if(c>=e){let f,g=b;if(b&256)f=a[a.length-1];else{if(d==null)return g;f=a[e+(+!!(b&512)-1)]={};g|=256}f[c]=d;c<e&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&(a[_.v]=g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b};_.Ab=function(a,b,c,d){a=a.ha;let e=a[_.v];d=_.zb(a,e,c,d);b=_.Xa(d,b,e);b!==d&&b!=null&&_.yb(a,e,c,b);return b};
_.Bb=function(a,b){return a!=null?a:b};
Eb=function(a){_.kb(a);var b=Cb?a.ha:fb(a.ha,hb,void 0,void 0,!1);var c=!Cb,d=(c?a.ha:b)[_.v];if(a=b.length){var e=b[a-1],f=Ea(e);f?a--:e=void 0;var g=+!!(d&512)-1,h=a-g;d=!!Db&&!(d&512);var k,l=(k=Db)!=null?k:ob;k=d?l(h,g,b,e):h;d=(h=d&&h!==k)?Array.prototype.slice.call(b,0,a):b;if(f||h){b:{var m=d;var p=e;var r;f=!1;if(h)for(l=Math.max(0,k+g);l<m.length;l++){var q=m[l];const D=l-g;if(!(q==null||Fa(q)||Da(q)&&q.size===0)){var w=m[l]=void 0;((w=r)!=null?w:r={})[D]=q;f=!0}}if(p)for(let D in p)if(w=
+D,isNaN(w)){let H;((H=r)!=null?H:r={})[D]=p[D]}else if(l=p[D],Array.isArray(l)&&(Fa(l)||Da(l)&&l.size===0)&&(l=null),l==null&&(f=!0),h&&w<k){f=!0;l=w+g;for(q=m.length;q<=l;q++)m.push(void 0);m[l]=p[w]}else if(l!=null){let H;((H=r)!=null?H:r={})[D]=l}f||(r=p);if(r)for(let D in r){p=r;break b}p=null}m=p==null?e!=null:p!==e}h&&(a=d.length);for(var C;a>0;a--){r=d[a-1];if(!(r==null||Fa(r)||Da(r)&&r.size===0))break;C=!0}if(d!==b||m||C){if(!h&&!c)d=Array.prototype.slice.call(d,0,a);else if(C||m||p)d.length=
a;p&&d.push(p)}b=d}return b};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Fb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Gb=function(a){for(const b in a)return!1;return!0};Hb=typeof Object.defineProperties=="function"?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
Ib=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Jb=Ib(this);Kb=function(a,b){if(b)a:{var c=Jb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Hb(c,a,{configurable:!0,writable:!0,value:b})}};
Kb("Symbol.dispose",function(a){return a?a:Symbol("b")});Kb("globalThis",function(a){return a||Jb});Kb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});var Nb,Ob,Rb;_.Lb=_.Lb||{};_.t=this||self;Nb=function(a,b){var c=_.Mb("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Ob=_.t._F_toggles||[];_.Mb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Qa=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Pb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Qb="closure_uid_"+(Math.random()*1E9>>>0);
Rb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Rb;return _.z.apply(null,arguments)};_.Sb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");var c=_.t;a[0]in c||typeof c.execScript=="undefined"||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.kj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Tb=!!(Ob[0]&8192),Ub=!!(Ob[0]&256),Vb=!!(Ob[0]>>14&1),Wb=!!(Ob[0]&64),Xb=!!(Ob[0]&32);var Yb,ha;Yb=Nb(1,!0);ha=Tb?Vb:Nb(610401301,!1);_.Zb=Tb?Ub||!Wb:Nb(653718497,Yb);_.$b=Tb?Xb:Nb(660014094,!1);_.ac=_.ba(a=>typeof a==="number");_.bc=_.ba(a=>typeof a==="string");_.cc=_.ba(a=>typeof a==="boolean");_.dc=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var gc,ec,hc,fc;_.$a=_.ba(a=>_.dc?a>=ec&&a<=fc:a[0]==="-"?ca(a,gc):ca(a,hc));gc=Number.MIN_SAFE_INTEGER.toString();ec=_.dc?BigInt(Number.MIN_SAFE_INTEGER):void 0;hc=Number.MAX_SAFE_INTEGER.toString();fc=_.dc?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.ic=typeof TextDecoder!=="undefined";_.jc=typeof TextEncoder!=="undefined";_.kc=function(){return _.fa().toLowerCase().indexOf("webkit")!=-1};var ia,lc=_.t.navigator;ia=lc?lc.userAgentData||null:null;_.ua=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.mc=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.nc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.oc=function(a){_.oc[" "](a);return a};_.oc[" "]=function(){};var Bc;_.pc=_.la();_.qc=_.ma();_.rc=_.u("Edge");_.sc=_.u("Gecko")&&!(_.kc()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.tc=_.kc()&&!_.u("Edge");_.uc=_.ta();_.vc=qa()?ia.platform==="Windows":_.u("Windows");_.wc=qa()?ia.platform==="Android":_.u("Android");_.xc=ra();_.yc=_.u("iPad");_.zc=_.u("iPod");_.Ac=_.sa();
a:{var Dc="",Ec=function(){var a=_.fa();if(_.sc)return/rv:([^\);]+)(\)|;)/.exec(a);if(_.rc)return/Edge\/([\d\.]+)/.exec(a);if(_.qc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(_.tc)return/WebKit\/(\S+)/.exec(a);if(_.pc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();Ec&&(Dc=Ec?Ec[1]:"");if(_.qc){var Fc,Gc=_.t.document;Fc=Gc?Gc.documentMode:void 0;if(Fc!=null&&Fc>parseFloat(Dc)){Bc=String(Fc);break a}}Bc=Dc}_.Hc=Bc;_.Ic=_.na();_.Jc=ra()||_.u("iPod");_.Kc=_.u("iPad");_.Lc=_.u("Android")&&!(oa()||_.na()||_.la()||_.u("Silk"));_.Mc=oa();_.Nc=_.pa()&&!_.sa();var Oc;_.v=Symbol();Oc=Symbol();_.Pc=Symbol();_.Qc=Symbol();var Ca,Sc;_.Wa={};Ca={};Sc=[];Sc[_.v]=55;_.Rc=Object.freeze(Sc);_.Tc=Object.freeze({});Object.freeze({});_.Uc=Object.freeze({});var Ja=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};var Vc;_.Xc=function(a,b){const c=_.Pa(a,b);c&&!_.Ma(a,c)&&(Na(),_.Wc(a,b))};_.kb=function(a){var b;if(a&&(b=_.Oa)!=null&&b.has(a)&&(b=a.ha))for(let c=0;c<b.length;c++){const d=b[c];if(c===b.length-1&&Ea(d))for(const e in d){const f=d[e];Array.isArray(f)&&_.Xc(f,a)}else Array.isArray(d)&&_.Xc(d,a)}};_.Oa=void 0;_.Wc=function(a,b){let c,d;(c=_.Oa)==null||(d=c.get(b))==null||d.delete(a)};var bb;_.Yc=function(a,b){a=a.ha;return _.zb(a,a[_.v],b)};_.zb=function(a,b,c,d){if(c===-1)return null;const e=b>>15&1023||536870912;if(c>=e){if(b&256)return a[a.length-1][c]}else{var f=a.length;if(d&&b&256&&(d=a[f-1][c],d!=null)){if(xb(a,b,e,c)&&Oc!=null){var g;a=(g=Vc)!=null?g:Vc={};g=a[Oc]||0;g>=4||(a[Oc]=g+1,_.Ka())}return d}return xb(a,b,e,c)}};_.Zc=function(a,b,c){const d=a.ha;let e=d[_.v];_.Ga(e);_.yb(d,e,b,c);return a};
_.E=function(a,b,c,d=!1){b=_.Ab(a,b,c,d);if(b==null)return b;a=a.ha;d=a[_.v];if(!(d&2)){const e=_.mb(b);e!==b&&(b=e,_.yb(a,d,c,b))}return b};_.F=function(a,b,c){c==null&&(c=void 0);return _.Zc(a,b,c)};_.G=function(a,b){a=_.Yc(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.I=function(a,b){return _.Va(_.Yc(a,b))};_.J=function(a,b,c=!1){return _.Bb(_.G(a,b),c)};_.K=function(a,b){return _.Bb(_.I(a,b),"")};_.M=function(a,b,c){return _.Zc(a,b,c==null?c:_.Ra(c))};
_.N=function(a,b,c){return _.Zc(a,b,c==null?c:_.Ta(c))};_.O=function(a,b,c){return _.Zc(a,b,_.Ua(c))};_.P=function(a,b,c){return _.Zc(a,b,c==null?c:_.Sa(c))};var Db,Cb;_.Q=class{constructor(a,b,c){this.ha=_.db(a,b,c)}toJSON(){return Eb(this)}Da(a){try{return Cb=!0,a&&(Db=a===ob||a!==nb&&a!==sb&&a!==vb?ob:a),JSON.stringify(Eb(this),Za)}finally{a&&(Db=void 0),Cb=!1}}vc(){return _.za(this.ha)}};_.Q.prototype.Dd=_.Wa;_.Q.prototype.toString=function(){try{return Cb=!0,Eb(this).toString()}finally{Cb=!1}};_.$c=Symbol();_.ad=Symbol();_.bd=Symbol();_.cd=Symbol();var dd=class extends _.Q{constructor(){super()}};_.ed=class extends _.Q{constructor(){super()}D(a){return _.N(this,3,a)}};var fd=class extends _.Q{constructor(a){super(a)}Mc(a){return _.O(this,24,a)}};_.gd=class extends _.Q{constructor(a){super(a)}};_.R=function(){this.ua=this.ua;this.Y=this.Y};_.R.prototype.ua=!1;_.R.prototype.isDisposed=function(){return this.ua};_.R.prototype.dispose=function(){this.ua||(this.ua=!0,this.P())};_.R.prototype[Symbol.dispose]=function(){this.dispose()};_.R.prototype.P=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var hd=class extends _.R{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){var b=this.o;a=a.split(".");for(var c=a.length,d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}tb(){for(var a=this.i.length,b=this.i,c=[],d=0;d<a;++d){var e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].tb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var jd=class extends _.R{constructor(){var a=_.id;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.kd=class extends _.Q{constructor(a){super(a)}};var ld=class extends _.Q{constructor(a){super(a)}};var od;_.md=function(a,b,c=98,d=new _.ed){if(a.i){const e=new dd;_.O(e,1,b.message);_.O(e,2,b.stack);_.N(e,3,b.lineNumber);_.P(e,5,1);_.F(d,40,e);a.i.log(c,d)}};od=class{constructor(){var a=nd;this.i=null;_.J(a,4,!0)}log(a,b,c=new _.ed){_.md(this,a,98,c)}};var pd,qd;pd=function(a){if(a.j.length>0){var b=a.oa!==void 0,c=a.i!==void 0;if(b||c){b=b?a.o:a.v;c=a.j;a.j=[];try{_.mc(c,b,a)}catch(d){console.error(d)}}}};_.rd=class{constructor(a){this.oa=a;this.i=void 0;this.j=[]}then(a,b,c){this.j.push(new qd(a,b,c));pd(this)}resolve(a){if(this.oa!==void 0||this.i!==void 0)throw Error("D");this.oa=a;pd(this)}reject(a){if(this.oa!==void 0||this.i!==void 0)throw Error("D");this.i=a;pd(this)}o(a){a.j&&a.j.call(a.i,this.oa)}v(a){a.o&&a.o.call(a.i,this.i)}};
qd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.sd=a=>{var b="tc";if(a.tc&&a.hasOwnProperty(b))return a.tc;b=new a;return a.tc=b};_.td=class{constructor(){this.v=new _.rd;this.i=new _.rd;this.D=new _.rd;this.B=new _.rd;this.C=new _.rd;this.A=new _.rd;this.o=new _.rd;this.j=new _.rd;this.F=new _.rd}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}ua(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.sd(_.td)}};var yd;_.vd=function(){return _.E(_.ud,fd,1)};_.wd=function(){return _.E(_.ud,_.gd,5)};yd=class extends _.Q{constructor(){super(xd)}};var xd;window.gbar_&&window.gbar_.CONFIG?xd=window.gbar_.CONFIG[0]||{}:xd=[];_.ud=new yd;var nd=_.E(_.ud,ld,3)||new ld;_.vd()||new fd;_.id=new od;_.A("gbar_._DumpException",function(a){_.id?_.id.log(a):console.error(a)});_.zd=new jd;var Bd;_.Cd=function(a,b){var c=_.Ad.i();if(a in c.i){if(c.i[a]!=b)throw new Bd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Gb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.Ad=class{constructor(){this.i={};this.j={}}static i(){return _.sd(_.Ad)}};_.Dd=class extends _.aa{constructor(){super()}};Bd=class extends _.Dd{};_.A("gbar.A",_.rd);_.rd.prototype.aa=_.rd.prototype.then;_.A("gbar.B",_.td);_.td.prototype.ba=_.td.prototype.M;_.td.prototype.bb=_.td.prototype.N;_.td.prototype.bd=_.td.prototype.ua;_.td.prototype.bf=_.td.prototype.Y;_.td.prototype.bg=_.td.prototype.L;_.td.prototype.bh=_.td.prototype.K;_.td.prototype.bj=_.td.prototype.J;_.td.prototype.bk=_.td.prototype.G;_.A("gbar.a",_.td.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var Ed=new hd;_.Cd("api",Ed);
var Fd=_.wd()||new _.gd,Gd=window,Hd=_.y(_.I(Fd,8));Gd.__PVT=Hd;_.Cd("eq",_.zd);
}catch(e){_._DumpException(e)}
try{
_.Id=class extends _.Q{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var Jd=class extends _.Q{constructor(){super()}};var Kd=class extends _.R{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b})}init(a,b,c){window.gapi={};var d=window.___jsl={};d.h=_.y(_.I(a,1));_.G(a,12)!=null&&(d.dpo=_.x(_.J(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.K(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.K(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var Ld=_.E(_.ud,_.kd,14);if(Ld){var Md=_.E(_.ud,_.Id,9)||new _.Id,Nd=new Jd,Od=new Kd;Od.init(Ld,Md,Nd);_.Cd("gs",Od)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_yovelakalista23@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./README_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20240924-060116_RC00_678132060'; var colabScsVersion = '9a0c2d97edb69755aa5bf3bc1065d5a5'; var hl = 'en-GB'; var colabExperiments = JSON.parse('\x7b\x22add_prompt_cell\x22: false, \x22ai_unsubscribed_warning\x22: false, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22cell_markdown_toolbar_tooltips\x22: false, \x22cell_output_actions_tooltip\x22: false, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: false, \x22cell_toolbar_tooltips\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: false, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22commands_in_toolbar\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: true, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: false, \x22embedded_connection_poll\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22execution_announcements\x22: true, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: false, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs\x22, \x22file_browser_poll_interval_millis\x22: 60000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22gemini_rebrand\x22: true, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_duplicate_code\x22: true, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: true, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22import_data\x22: false, \x22import_gemini_api_key\x22: false, \x22interactive_sheet_next_steps\x22: true, \x22internal_chat\x22: false, \x22internal_schedule\x22: false, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22min_dep_cells_runtime_kernel_cl\x22: 669325580, \x22ml_enabled\x22: true, \x22mlpp\x22: false, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22pds_minting\x22: false, \x22prereq_cells_next_steps\x22: true, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_chat_not_answering\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_dap\x22: true, \x22rp_kws\x22: false, \x22rp_kxhr\x22: true, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: false, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt\x22: false, \x22run_mode\x22: true, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting\x22: false, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_create_gemini_api_key_link\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: false, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.25\x22, \x22smartpaste_tooltip\x22: false, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22suspicious_code_matches\x22: \x22\x22, \x22suspicious_code_regexs\x22: \x22\x22, \x22term4all\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: false, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_corplogin\x22: true, \x22use_dm_sql_lsp\x22: false, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22waffle\x22: false, \x22workstations\x22: false, \x22ids\x22: \x5b20730185, 20730297, 20730177, 20730265, 20730262, 20730183, 20730230, 20730150\x5d, \x22flag_ids\x22: \x7b\x22add_prompt_cell\x22: 45644995, \x22ai_unsubscribed_warning\x22: 45504730, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22allowed_public_url_domains\x22: 45425558, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22cell_markdown_toolbar_tooltips\x22: 45654223, \x22cell_output_actions_tooltip\x22: 45650940, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_toolbar_tooltips\x22: 45649981, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22embedded_connection_poll\x22: 45491618, \x22enable_adhoc_backends\x22: 45425506, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22execution_announcements\x22: 45651325, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22gemini_rebrand\x22: 45631310, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_duplicate_code\x22: 45646291, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22interactive_sheet_next_steps\x22: 45634324, \x22internal_chat\x22: 45622872, \x22internal_schedule\x22: 45425578, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mlpp\x22: 45425608, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22mpp_orc_temperature_override\x22: 45649914, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22pds_minting\x22: 45648255, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_chat_not_answering\x22: 45640977, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_dap\x22: 45649113, \x22rp_kws\x22: 45650184, \x22rp_kxhr\x22: 45491686, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt\x22: 45425624, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting\x22: 45647313, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_create_gemini_api_key_link\x22: 45644190, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22smartpaste_tooltip\x22: 45653721, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22suspicious_code_matches\x22: 45425615, \x22suspicious_code_regexs\x22: 45425616, \x22term4all\x22: 45425542, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_corplogin\x22: 45425606, \x22use_dm_sql_lsp\x22: 45425610, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22waffle\x22: 45446491, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'yovelakalista23@gmail.com'; var colabRenderDataToken = 'AFWLbD1SKTqIwVwCBrIEOP4POcoQR3xYm72Z9YuUUo3Qr7Gh_DKLz19Mfk0I304tbNhc7gR2vHuOAZakCUw2CpN4BgGoWfa-ZylG2GLa'; var colabConfig = '\x5b\x5b\x22yovelakalista23@gmail.com\x22,\x5b1,\x22AHXL0D0qcLwhgqSqEEeseAaju02cKmGoGdyqlctgfjrWcrIJdWXq23vqgA1\/bDLK6bsD9CaBkU6zXsF\/gP69ruIFG6sFd80ovMk6LXlrBxG4M+2awPQtOP8+5zaVe\/ZAO5SnwyWYnKwCnFH8jxcZn3hPLznsg+hV0VrYbeHh+ukKWBLQum81iTceXZekcCArMclSJgO8uojelUa0igzyLmFjPOxlFB3qr33EbMFZT+KciA1AXdEQISt\/23HPxgT1ZmkP6CtFs2ONYgkfw2R+XhCHNulfhu8DYnAp97aWwNlKXT+IHYOr17zhIJbK5EoCjJm3EVHjiuX26MYwFwarXSz6qPSN4RoSto3bmRa63C8Gz3tIMeUiIoIOORH9Ya7s\/cH+v4cunnwKNMyMoZ6ScXFDimPND6vs92p4Vnx7a833fHKPtvDNbQljnLShLa7drN0DZJhnWRwSExe5fw7178p8uN9JmR9QRke\/LRd8+80M4rhGjRSsUoUnPYfRQdZMLOL1VVJTkH2o3cmH6P6ph4jeIYwaL2nAl24ZDt1pkXRQ4\/3Z1LAVz0y6edotAUX\/Y7NaMRswQyjody4H4C7drtjZTrZOaORSyRJjiKTBip80M\/\/G0ccLdgAgXzSXncZETfNO9TwUuvLpaMj7YyHJD6NZo9ChrsrvKchDR4tC3y2na55jUJUdEyVrNjtiYFoJclVDZLyTlhnaCUwdmPbUkJsg0W+6s91tDx3usWOc8BasnPvzh\/XaMBUuxQCIc6vEKmjMW\/vBGcHuWBKG3I3cT0Te1cyBLcUJGDBWSzwa4iubUQmtUwyldrfukYQlcnSBMhwv3UFRn1j7UpKKSQJ8mHYt8D9+Is60yHnwC2YJOhD5xYO5RXWJURFro9N1A+\/ifsy\/QK6sDp9NVk4OC9JrFGZc1F\/KIdTwnalla0Lz3wggeJIwkzwPlOzLGEf4o\/9Wu8odvboYVHmJdj2nqpT\/urd51iCGIh\/8LHRRBntKja2vpxrczbR1tpPWp+LBqg6lyJcCx9M8OSEdi0wiX+WilYVRp1HbAFbet\/5kqRKx7f2Xu+WrOWcMsUFs2u2v9s+RMj6G5k6F9US9cuLP+i86xF0j9UK8P\/6miJU7dkf5VEtyE5pxdjKHeT3KmWMO1OWqJ0I9QSxp\/sUoU+viq0JcOEESe+ww1EMMOktNrn1oyQHZNWj8okAzZHVni+3ZNNzZLtr9mL9eiHDlCjmMlVMUWr2liVArVef1lv12Dx6K4RXsi36BEPdeAhLgUj35Wae1YxG+d566MSRUN3N5FqlYO0rZsy5Jvu5Db3gc0S+ZTGbqoCgmn4FOAD5e55fPJb6f9mcC9jdJ5QnbovY0ZTeKFQk892GnGH4xy4Z2xUq5YHhSFlgW1mm+KHAB7JRHlPxCq48o\/HsTaRNnjNpandU9gW\/vJbkTz8c+y3J3BEEwjNMuTpNtcA0BrBwF7ncGd3muodowHGPITY\/c+9sxsASFCw4bqu\/VHg2wcJUwq3d2tAdnJAfggTf49bEOK2tx+B\/qI8XVF2vQkZhB6lDN2bGXCZml7IaWR9dI15OrONbEDjuF2Y\/RB0ZydtwjeMINOEulDHbLSNooD+RjLv6HL13wsWvlkpmlgZNW7y4bDHCM+azikJHCaDfPka3ylrQJPgmfI9OXivJ4jXkq7wCKCZUsIT0uylSwMEtqwfbk1+DnYmTbPERZw3CSx9XwrGDtQOXg1CBsU89EsdijpquCRej1gMmfC0Cp5FuREsvefPgbWg\/9Nqzr92pv+DX7c64MxFPelGnQArthoweGkCM\/r4k2qBTkitqHUs+YXEB5CtEPTDxG8Cx8M9w1JRso3aGzoOP7CpNg2u5O03k+3cEHzRAfDilFNGajgDh4Rd5XOilOJzigHnrvlZo7984\x3d\x22,\x22AJ9oCCwdwVPSHCd6C0yGe8G3FPFOdYKqOK525zMhxpFzuM8rBK9jg2A8OF9jvTDCGGuT7sV6nBrCjmsUX32PChfFPW747cWIC2vBm3OnCr+hUM1o7qg+PcYG+6Nhd5QUpvwKajsVCXyN\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22US$9,99\x22,\x22US$49,99\x22,\x22US$9,99\x22,\x22US$49,99\x22\x5d,\x5b1,4,5\x5d,\x22ID\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/9a0c2d97edb69755aa5bf3bc1065d5a5/img%2Ffavicon_error.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="-wL8iYJTC7X0zF9qBNDQUAd-P1ZkQUK-OhSgv4Wkf1M"><meta name="google-site-verification" content="o-EECwEDQeUpZv0jTmoGfCDX7dUI8Kul4ESepXmDnO0"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./README_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><script async="async" type="text/javascript" src="./README_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./README_files/rs=AA2YrTv3Qzh6Ja6eSLzWU_FOQIMZM5uKUQ" nonce=""></script><link type="text/css" href="./README_files/rs=AA2YrTt6If9d1pi4yP4MpRCU4A1M3rvNtg" rel="stylesheet"><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./README_files/editor.main.css"><script async="async" type="text/javascript" src="./README_files/editor.main.nls.js.download"></script><script async="async" type="text/javascript" src="./README_files/markdown.js.download"></script><script src="./README_files/api.js.download" nonce=""></script><script src="./README_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #f7f7f7; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #f7f7f7;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #f7f7f7;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: #616161;
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: #616161;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: #616161;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: #616161;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-insertedLineBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #e4e4e4;
--vscode-diffEditor-unchangedRegionForeground: #4d4c4c;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #f7f7f7;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #f7f7f7;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0.08);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #f7f7f7;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #f7f7f7; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #e00000; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #795e26; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #af00db; }
.mtk20 { color: #c43b3b; }
.mtk21 { color: #800000; }
.mtk22 { color: #3030c0; }
.mtk23 { color: #666666; }
.mtk24 { color: #778899; }
.mtk25 { color: #c700c7; }
.mtk26 { color: #a31515; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #008080; }
.mtk29 { color: #001188; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><script src="./README_files/api(2).js.download" nonce=""></script><script src="./README_files/api(3).js.download" nonce=""></script><script async="async" type="text/javascript" src="./README_files/python.js.download"></script></head><body class="" data-new-gr-c-s-check-loaded="14.1196.0" data-gr-ext-installed="" style="overscroll-behavior: contain;" data-new-gr-c-s-loaded="14.1197.0"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./README_files/gapi_loader.js.download" nonce=""></script><script src="./README_files/socketio_binary.js.download" nonce=""></script><script src="./README_files/analytics_binary.js.download" nonce=""></script><script src="./README_files/MathJax.js.download" nonce=""></script><script src="./README_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./README_files/external_binary_l10n__en_gb.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$742065472$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$742065472$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$742065472$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$742065472$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Loading…</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Sd;Sd=class extends _.Dd{};_.Td=function(a,b){if(b in a.i)return a.i[b];throw new Sd;};_.Ud=function(a){return _.Td(_.Ad.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Xd;_.Vd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Xd=function(a){return new _.Wd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Yd=globalThis.trustedTypes;_.Zd=class{constructor(a){this.i=a}toString(){return this.i}};_.$d=new _.Zd("about:invalid#zClosurez");_.Wd=class{constructor(a){this.Yg=a}};_.ae=[Xd("data"),Xd("http"),Xd("https"),Xd("mailto"),Xd("ftp"),new _.Wd(a=>/^[^:]*([/?#]|$)/.test(a))];_.be=class{constructor(a){this.i=a}toString(){return this.i+""}};_.ce=new _.be(_.Yd?_.Yd.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var ge,ue,fe,he,me;_.de=function(a){return a==null?a:Number.isFinite(a)?a|0:void 0};_.ee=function(a){if(a==null)return a;if(typeof a==="string"){if(!a)return;a=+a}if(typeof a==="number")return Number.isFinite(a)?a|0:void 0};ge=function(){let a=null;if(!fe)return a;try{const b=c=>c;a=fe.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.ie=function(){he===void 0&&(he=ge());return he};
_.ke=function(a){const b=_.ie();return new _.je(b?b.createScriptURL(a):a)};_.le=function(a){if(a instanceof _.je)return a.i;throw Error("F");};_.ne=function(a){if(me.test(a))return a};_.oe=function(a){if(a instanceof _.Zd)if(a instanceof _.Zd)a=a.i;else throw Error("F");else a=_.ne(a);return a};_.pe=function(a,b){let c,d;return(b=(d=(c=b.document).querySelector)==null?void 0:d.call(c,`${a}[nonce]`))?b.nonce||b.getAttribute("nonce")||"":""};
_.qe=function(a){var b=_.Qa(a);return b=="array"||b=="object"&&typeof a.length=="number"};_.re=function(a,b,c){return _.Ab(a,b,c,!1)!==void 0};_.se=function(a,b){return _.ee(_.Yc(a,b))};_.S=function(a,b){return _.de(_.Yc(a,b))};_.T=function(a,b,c=0){return _.Bb(_.se(a,b),c)};_.te=function(a,b,c=0){return _.Bb(_.S(a,b),c)};_.ve=function(a,b){return a.lastIndexOf(b,0)==0};fe=_.Yd;_.je=class{constructor(a){this.i=a}toString(){return this.i+""}};me=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var Be,Fe,we;_.ye=function(a){return a?new we(_.xe(a)):ue||(ue=new we)};_.ze=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.U=function(a,b){var c=b||document;if(c.getElementsByClassName)a=c.getElementsByClassName(a)[0];else{c=document;var d=b||c;a=d.querySelectorAll&&d.querySelector&&a?d.querySelector(a?"."+a:""):_.Ae(c,a,b)[0]||null}return a||null};
_.Ae=function(a,b,c){var d;a=c||a;if(a.querySelectorAll&&a.querySelector&&b)return a.querySelectorAll(b?"."+b:"");if(b&&a.getElementsByClassName){var e=a.getElementsByClassName(b);return e}e=a.getElementsByTagName("*");if(b){var f={};for(c=d=0;a=e[c];c++){var g=a.className;typeof g.split=="function"&&_.va(g.split(/\s+/),b)&&(f[d++]=a)}f.length=d;return f}return e};
_.Ce=function(a,b){_.Fb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:Be.hasOwnProperty(d)?a.setAttribute(Be[d],c):_.ve(d,"aria-")||_.ve(d,"data-")?a.setAttribute(d,c):a[d]=c})};Be={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.De=function(a){return a?a.defaultView:window};_.Ge=function(a,b){var c=b[1],d=_.Ee(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.Ce(d,c));b.length>2&&Fe(a,d,b);return d};Fe=function(a,b,c){function d(g){g&&b.appendChild(typeof g==="string"?a.createTextNode(g):g)}for(var e=2;e<c.length;e++){var f=c[e];!_.qe(f)||_.Pb(f)&&f.nodeType>0?d(f):_.mc(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Vd(f):f,d)}};
_.He=function(a){return _.Ee(document,a)};_.Ee=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.Ie=function(a){for(var b;b=a.firstChild;)a.removeChild(b)};_.Je=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.Ke=function(a,b){return a&&b?a==b||a.contains(b):!1};_.xe=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};we=function(a){this.i=a||_.t.document||document};_.n=we.prototype;
_.n.H=function(a){return _.ze(this.i,a)};_.n.ab=function(a,b,c){return _.Ge(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.te=_.Ie;_.n.Of=_.Je;_.n.Nf=_.Ke;
}catch(e){_._DumpException(e)}
try{
_.Xi=function(a){const b=_.pe("script",a.ownerDocument&&a.ownerDocument.defaultView||window);b&&a.setAttribute("nonce",b)};_.Yi=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.ke(a);return b};_.Zi=class extends _.Q{constructor(a){super(a)}};_.$i=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var bj=function(a,b,c){a<b?aj(a+1,b):_.id.log(Error("ea`"+a+"`"+b),{url:c})},aj=function(a,b){if(cj){const c=_.He("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.le(cj);_.Xi(c);c.onerror=_.Sb(bj,a,b,c.src);_.$i("HEAD")[0].appendChild(c)}},dj=class extends _.Q{constructor(a){super(a)}};var ej=_.E(_.ud,dj,17)||new dj,fj,cj=(fj=_.E(ej,_.Zi,1))?_.Yi(fj):null,gj,hj=(gj=_.E(ej,_.Zi,2))?_.Yi(gj):null,ij=function(){aj(1,2);if(hj){const a=_.He("LINK");a.setAttribute("type","text/css");a.href=_.le(hj).toString();a.rel="stylesheet";let b=_.pe("style",window);b&&a.setAttribute("nonce",b);_.$i("HEAD")[0].appendChild(a)}};(function(){const a=_.vd();if(_.G(a,18))ij();else{const b=_.se(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(ij,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div class="gb_S" ng-non-bindable=""><div class="gb_Bc"><div>Google Account</div><div class="gb_g">Yovela Kalista</div><div>yovelakalista23@gmail.com</div></div></div><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="apiproxy65b287372fc0ba43961ce7041d6beb1069a077930.186694555" name="apiproxy65b287372fc0ba43961ce7041d6beb1069a077930.186694555" src="./README_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><iframe src="./README_files/bscframe.html" style="display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-dr8bo9u2gh8j" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./README_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./README_files/saved_resource.html"></iframe></div><iframe id="hfcr" src="./README_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <div class="top-floater"><div role="banner">
    <colab-header-skip-button><template shadowrootmode="open"><!----><a id="skiplink" class="skip-link" href="https://colab.research.google.com/drive/1oWls66ZouV9nqiLH9ldCNUYAvRMF1mr1#top-toolbar"><!--?lit$742065472$-->Skip to main content</a></template></colab-header-skip-button>
    <!--?lit$742065472$-->
    <!--?lit$742065472$-->
    <!--?lit$742065472$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning hidden">
            <!--?lit$742065472$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1oWls66ZouV9nqiLH9ldCNUYAvRMF1mr1#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
          <mwc-icon-button class="close" icon="close" title="Close"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Close"><!--?lit$742065472$-->
    <!--?lit$742065472$--><i class="material-icons"><!--?lit$742065472$-->close</i>
    <span><slot></slot></span>
  </button></template></mwc-icon-button></div>
        

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><div id="header-logo">
              <!--?lit$742065472$--> <!--?lit$742065472$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$742065472$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$742065472$--> <!--?lit$742065472$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 110.125px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">README.md_</colab-input-sizer>
            <!--?lit$742065472$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$742065472$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$742065472$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$742065472$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$742065472$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$742065472$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$742065472$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$742065472$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$742065472$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div>
    <div id="colab-menu-cover" style="display: none;"> </div></div><!----><colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$742065472$-->All changes saved</button></template></colab-last-saved-indicator></div></div>
        <div id="header-right">
          <!--?lit$742065472$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$742065472$-->
      <!--?lit$742065472$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$742065472$--> <md-text-button id="comments" command="open-comments-thread" aria-describedby="comments-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
                <!--?lit$742065472$-->Comment
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$742065472$--> <md-text-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->people</md-icon>
                <!--?lit$742065472$-->Share
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$742065472$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$742065472$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->search</md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variables" title="Variables" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Variables" aria-pressed="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->folder</md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button command="snippets" data-aria-label="Code snippets" title="Code snippets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->code</md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button command="show-command-palette" data-aria-label="Command palette" title="Command palette" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Command palette">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg></md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$742065472$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->terminal</md-icon>
    </md-icon-button> <!--?lit$742065472$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$742065472$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
        <!--?lit$742065472$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$742065472$--><span class="screenreader-only"><!--?lit$742065472$-->Insert code cell below <!--?lit$742065472$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$742065472$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$742065472$-->Code
          </colab-toolbar-button>
          <!--?lit$742065472$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
        <!--?lit$742065472$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$742065472$--><span class="screenreader-only"><!--?lit$742065472$-->Add text cell <!--?lit$742065472$--></span>
      </md-text-button>
      <!--?lit$742065472$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$742065472$-->Text
          </colab-toolbar-button>
        
    <!--?lit$742065472$-->
    <!--?lit$742065472$-->
    <!--?lit$742065472$-->
    <!--?lit$742065472$-->
    <!--?lit$742065472$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$742065472$-->All changes saved</button></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$742065472$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$742065472$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$742065472$--><!--?lit$742065472$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$742065472$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connected to
Python 3 Google Compute Engine backend
RAM: 1.12 GB/12.67 GB
Disk: 36.46 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
        <!--?lit$742065472$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$742065472$--><span class="screenreader-only"><!--?lit$742065472$-->Connected to
Python 3 Google Compute Engine backend
RAM: 1.12 GB/12.67 GB
Disk: 36.46 GB/107.72 GB <!--?lit$742065472$--></span>
      </md-text-button>
      <!--?lit$742065472$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connected to
Python 3 Google Compute Engine backend
RAM: 1.12 GB/12.67 GB
Disk: 36.46 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Connected to</div><!----><!----><div><!--?lit$742065472$-->Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$742065472$-->RAM: 1.12 GB/12.67 GB</div><!----><!----><div><!--?lit$742065472$-->Disk: 36.46 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$742065472$--> <div id="connect-button-resource-display">
        <!--?lit$742065472$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$742065472$-->RAM</div>
      <!--?lit$742065472$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        <!--?lit$742065472$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$742065472$-->Disk</div>
      <!--?lit$742065472$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
      </div>
      </colab-toolbar-button>
      <!--?lit$742065472$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$742065472$--> <span class="colab-separator"></span>
          <colab-toolbar-button command="show-chat" icon="spark"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
        <!--?lit$742065472$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->spark</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$742065472$--><span class="screenreader-only"><!--?lit$742065472$--> <!--?lit$742065472$--></span>
      </md-text-button>
      <!--?lit$742065472$--><!--?--></template>
            <!--?lit$742065472$-->Gemini
          </colab-toolbar-button>
    <!--?lit$742065472$-->
    <span class="collapsed-options">
      <!--?lit$742065472$--><span class="colab-separator"></span>
      <!--?lit$742065472$--> <md-icon-button command="share" title="Share notebook" data-aria-label="Share notebook" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->people</md-icon>
          </md-icon-button><md-icon-button command="preferences" data-aria-label="Open settings" title="Open settings" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$742065472$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$742065472$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$742065472$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-jkY_sIyZO4ZW" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$742065472$--><div class="indicator"></div>
      </div>
      <!--?lit$742065472$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-jkY_sIyZO4ZW"><!--?lit$742065472$--><!--?lit$742065472$-->Notebook<!--?--></span>
            <!--?lit$742065472$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$742065472$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" role="main" class="notebook-container" aria-label="Notebook" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$742065472$-->
              <div class="notebook-content ">
                <!--?lit$742065472$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell text" id="cell-qMz0BCihk6DM" tabindex="-1" role="region" aria-label="Cell 0: Text cell: HOW TO RUN DASHBOARD" style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"><div class="markdown-toolbar"><!----><!--?lit$742065472$--><!----><md-icon-button id="markdown-toolbar-header-qMz0BCihk6DM" class="markdown-toolbar-header" title="Toggle heading" data-aria-label="Toggle heading" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle heading">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_size</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-bold-qMz0BCihk6DM" class="markdown-toolbar-bold" title="Bold" data-aria-label="Bold" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bold">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_bold</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-italic-qMz0BCihk6DM" class="markdown-toolbar-italic" title="Italicise" data-aria-label="Italicise" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Italicise">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_italic</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-code-qMz0BCihk6DM" class="markdown-toolbar-code" title="Format as code" data-aria-label="Format as code" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Format as code">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->code</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-link-qMz0BCihk6DM" class="markdown-toolbar-link" title="Insert link" data-aria-label="Insert link" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert link">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->link</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><label for="markdown-image-input-qMz0BCihk6DM" class="colab-icon markdown-toolbar-insert-image">
        <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <span role="button" tabindex="0" id="markdown-toolbar-insert-image-qMz0BCihk6DM" title="Insert image" aria-label="Insert image">
          <md-focus-ring aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>image</md-icon>
        </span>
        <!--?lit$742065472$-->
      </label>
      <input class="markdown-image-input" type="file" multiple="" accept="image/*" id="markdown-image-input-qMz0BCihk6DM"><!----><!----><md-icon-button id="markdown-toolbar-blockquote-qMz0BCihk6DM" class="markdown-toolbar-blockquote" title="Add blockquote" data-aria-label="Add blockquote" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add blockquote">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_quote</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ol-qMz0BCihk6DM" class="markdown-toolbar-ol" title="Add numbered list" data-aria-label="Add numbered list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add numbered list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_numbered</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ul-qMz0BCihk6DM" class="markdown-toolbar-ul" title="Add bulleted list" data-aria-label="Add bulleted list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add bulleted list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_bulleted</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-hr-qMz0BCihk6DM" class="markdown-toolbar-hr" title="Add horizontal rule" data-aria-label="Add horizontal rule" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add horizontal rule">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->horizontal_rule</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-latex-qMz0BCihk6DM" class="markdown-toolbar-latex" title="LaTeX" data-aria-label="LaTeX" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="LaTeX">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><span aria-hidden="true">ψ</span>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-emoji-qMz0BCihk6DM" class="markdown-toolbar-emoji" title="Insert emoji" data-aria-label="Insert emoji" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert emoji">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->mood</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-preview-qMz0BCihk6DM" class="markdown-toolbar-preview" title="Reposition markdown preview" data-aria-label="Reposition markdown preview" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Reposition markdown preview">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$--><g id="markdown-preview-below">
  <rect width="20" height="18" x="2" y="2" rx="2" ry="2" style="fill:none;stroke:var(--colab-icon-color)"></rect>
  <line x1="4.5" y1="13" x2="19.5" y2="13" style="stroke:var(--colab-primary-text-color);stroke-dasharray:2"></line>
  <line x1="2.5" y1="4" x2="21.5" y2="4" style="stroke:var(--colab-icon-color);stroke-width:3px;"></line>
</g></svg></md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!--?--></div></div>
      <div class="editor-container horizontal">
        <div class="editor-root"><div class="editor flex monaco" data-keybinding-context="2" data-mode-id="markdown" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off; display: none;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/22" style="width: 338px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 338px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 332px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 332px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:332px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 332px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">#&nbsp;**HOW&nbsp;TO&nbsp;RUN&nbsp;DASHBOARD**</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 332px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 184px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 318px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 318px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="29" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 338px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 316px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 338px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 684px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 0 child cells under HOW TO RUN DASHBOARD (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 0 child cells under HOW TO RUN DASHBOARD (Press &lt;Shift&gt; to also collapse sibling sections)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 0 child cells under HOW TO RUN DASHBOARD (Press &lt;Shift&gt; to also collapse sibling sections)">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1><strong>HOW TO RUN DASHBOARD</strong></h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Run cell">
        <span class="execution-count"><!--?lit$742065472$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$742065472$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$742065472$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$742065472$--> <!--?lit$742065472$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div></div><div class="cell text" id="cell-OkUi1VAxlA1Y" tabindex="-1" role="region" aria-label="Cell 1: Text cell: Setup environment - Anaconda" style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"><div class="markdown-toolbar"><!----><!--?lit$742065472$--><!----><md-icon-button id="markdown-toolbar-header-OkUi1VAxlA1Y" class="markdown-toolbar-header" title="Toggle heading" data-aria-label="Toggle heading" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle heading">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_size</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-bold-OkUi1VAxlA1Y" class="markdown-toolbar-bold" title="Bold" data-aria-label="Bold" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bold">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_bold</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-italic-OkUi1VAxlA1Y" class="markdown-toolbar-italic" title="Italicise" data-aria-label="Italicise" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Italicise">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_italic</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-code-OkUi1VAxlA1Y" class="markdown-toolbar-code" title="Format as code" data-aria-label="Format as code" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Format as code">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->code</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-link-OkUi1VAxlA1Y" class="markdown-toolbar-link" title="Insert link" data-aria-label="Insert link" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert link">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->link</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><label for="markdown-image-input-OkUi1VAxlA1Y" class="colab-icon markdown-toolbar-insert-image">
        <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <span role="button" tabindex="0" id="markdown-toolbar-insert-image-OkUi1VAxlA1Y" title="Insert image" aria-label="Insert image">
          <md-focus-ring aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>image</md-icon>
        </span>
        <!--?lit$742065472$-->
      </label>
      <input class="markdown-image-input" type="file" multiple="" accept="image/*" id="markdown-image-input-OkUi1VAxlA1Y"><!----><!----><md-icon-button id="markdown-toolbar-blockquote-OkUi1VAxlA1Y" class="markdown-toolbar-blockquote" title="Add blockquote" data-aria-label="Add blockquote" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add blockquote">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_quote</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ol-OkUi1VAxlA1Y" class="markdown-toolbar-ol" title="Add numbered list" data-aria-label="Add numbered list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add numbered list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_numbered</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ul-OkUi1VAxlA1Y" class="markdown-toolbar-ul" title="Add bulleted list" data-aria-label="Add bulleted list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add bulleted list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_bulleted</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-hr-OkUi1VAxlA1Y" class="markdown-toolbar-hr" title="Add horizontal rule" data-aria-label="Add horizontal rule" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add horizontal rule">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->horizontal_rule</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-latex-OkUi1VAxlA1Y" class="markdown-toolbar-latex" title="LaTeX" data-aria-label="LaTeX" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="LaTeX">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><span aria-hidden="true">ψ</span>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-emoji-OkUi1VAxlA1Y" class="markdown-toolbar-emoji" title="Insert emoji" data-aria-label="Insert emoji" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert emoji">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->mood</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-preview-OkUi1VAxlA1Y" class="markdown-toolbar-preview" title="Reposition markdown preview" data-aria-label="Reposition markdown preview" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Reposition markdown preview">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$--><g id="markdown-preview-below">
  <rect width="20" height="18" x="2" y="2" rx="2" ry="2" style="fill:none;stroke:var(--colab-icon-color)"></rect>
  <line x1="4.5" y1="13" x2="19.5" y2="13" style="stroke:var(--colab-primary-text-color);stroke-dasharray:2"></line>
  <line x1="2.5" y1="4" x2="21.5" y2="4" style="stroke:var(--colab-icon-color);stroke-width:3px;"></line>
</g></svg></md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!--?--></div></div>
      <div class="editor-container horizontal">
        <div class="editor-root"><div class="editor flex monaco" data-keybinding-context="3" data-mode-id="markdown" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off; display: none;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/23" style="width: 338px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 338px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 332px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 332px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:332px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 332px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">#&nbsp;Setup&nbsp;environment&nbsp;-&nbsp;Anaconda</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 332px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 230px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 318px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 318px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="29" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 338px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 316px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 338px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 684px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 1 child cell under Setup environment - Anaconda (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 1 child cell under Setup environment - Anaconda (Press &lt;Shift&gt; to also collapse sibling sections)" style="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 1 child cell under Setup environment - Anaconda (Press &lt;Shift&gt; to also collapse sibling sections)">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>Setup environment - Anaconda</h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Run cell">
        <span class="execution-count"><!--?lit$742065472$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$742065472$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$742065472$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$742065472$--> <!--?lit$742065472$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 1 cell hidden</div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling" id="cell-mW9WZk43O4Y-" role="region" aria-label="Cell 2: Code cell: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell">
        <span class="execution-count"><!--?lit$742065472$-->[2]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$742065472$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$742065472$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$742065472$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change
Previous execution ended unsuccessfully"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$742065472$-->cell executed since last change</div><!----><!----><div><!--?lit$742065472$-->Previous execution ended unsuccessfully</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$742065472$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$742065472$--></div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="13" data-mode-id="notebook-python" style="height: 67px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/21" style="width: 627px; height: 67px;"><div data-mprt="3" class="overflow-guard" style="width: 627px; height: 67px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 67px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 67px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 67px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 621px; height: 67px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 67px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 621px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:621px; height:19px;"></div><div class="cdr squiggly-warning" style="left:0px;width:38px;height:19px;"></div><div class="cdr squiggly-warning" style="left:46px;width:46px;height:19px;"></div><div class="cdr squiggly-warning" style="left:115px;width:31px;height:19px;"></div><div class="cdr squiggly-warning" style="left:154px;width:31px;height:19px;"></div><div class="cdr squiggly-warning" style="left:192px;width:15px;height:19px;"></div><div class="cdr squiggly-error" style="left:0px;width:293px;height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:0px;width:38px;height:19px;"></div><div class="cdr squiggly-warning" style="left:46px;width:62px;height:19px;"></div><div class="cdr squiggly-warning" style="left:115px;width:31px;height:19px;"></div><div class="cdr squiggly-warning" style="left:154px;width:15px;height:19px;"></div><div class="cdr squiggly-error" style="left:46px;width:62px;height:19px;"></div><div class="cdr squiggly-error" style="left:115px;width:31px;height:19px;"></div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:0px;width:23px;height:19px;"></div><div class="cdr squiggly-warning" style="left:31px;width:54px;height:19px;"></div><div class="cdr squiggly-warning" style="left:100px;width:8px;height:19px;"></div><div class="cdr squiggly-warning" style="left:115px;width:92px;height:19px;"></div><div class="cdr squiggly-error" style="left:31px;width:54px;height:19px;"></div><div class="cdr squiggly-error" style="left:115px;width:92px;height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 621px; height: 67px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk1">conda&nbsp;create&nbsp;--name&nbsp;main-ds&nbsp;python=</span><span class="mtk12">3.9</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1">conda&nbsp;activate&nbsp;main-ds</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">pip&nbsp;install&nbsp;-r&nbsp;requirements.txt</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 621px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 607px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 607px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="67" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 67px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 67px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 67px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 627px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 627px;"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 67px;"><div class="minimap-shadow-hidden" style="height: 67px;"></div><canvas width="0" height="67" style="position: absolute; left: 0px; width: 0px; height: 67px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="67" style="position: absolute; left: 0px; width: 0px; height: 67px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 684px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"></div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer" style="min-height: 0px;"> </div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div></div><div class="cell text" id="cell-3gDOjDymlE5d" tabindex="-1" role="region" aria-label="Cell 3: Text cell: Setup Environment - Shell/Terminal" style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"><div class="markdown-toolbar"><!----><!--?lit$742065472$--><!----><md-icon-button id="markdown-toolbar-header-3gDOjDymlE5d" class="markdown-toolbar-header" title="Toggle heading" data-aria-label="Toggle heading" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle heading">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_size</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-bold-3gDOjDymlE5d" class="markdown-toolbar-bold" title="Bold" data-aria-label="Bold" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bold">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_bold</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-italic-3gDOjDymlE5d" class="markdown-toolbar-italic" title="Italicise" data-aria-label="Italicise" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Italicise">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_italic</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-code-3gDOjDymlE5d" class="markdown-toolbar-code" title="Format as code" data-aria-label="Format as code" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Format as code">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->code</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-link-3gDOjDymlE5d" class="markdown-toolbar-link" title="Insert link" data-aria-label="Insert link" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert link">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->link</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><label for="markdown-image-input-3gDOjDymlE5d" class="colab-icon markdown-toolbar-insert-image">
        <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <span role="button" tabindex="0" id="markdown-toolbar-insert-image-3gDOjDymlE5d" title="Insert image" aria-label="Insert image">
          <md-focus-ring aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>image</md-icon>
        </span>
        <!--?lit$742065472$-->
      </label>
      <input class="markdown-image-input" type="file" multiple="" accept="image/*" id="markdown-image-input-3gDOjDymlE5d"><!----><!----><md-icon-button id="markdown-toolbar-blockquote-3gDOjDymlE5d" class="markdown-toolbar-blockquote" title="Add blockquote" data-aria-label="Add blockquote" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add blockquote">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_quote</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ol-3gDOjDymlE5d" class="markdown-toolbar-ol" title="Add numbered list" data-aria-label="Add numbered list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add numbered list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_numbered</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ul-3gDOjDymlE5d" class="markdown-toolbar-ul" title="Add bulleted list" data-aria-label="Add bulleted list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add bulleted list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_bulleted</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-hr-3gDOjDymlE5d" class="markdown-toolbar-hr" title="Add horizontal rule" data-aria-label="Add horizontal rule" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add horizontal rule">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->horizontal_rule</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-latex-3gDOjDymlE5d" class="markdown-toolbar-latex" title="LaTeX" data-aria-label="LaTeX" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="LaTeX">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><span aria-hidden="true">ψ</span>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-emoji-3gDOjDymlE5d" class="markdown-toolbar-emoji" title="Insert emoji" data-aria-label="Insert emoji" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert emoji">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->mood</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-preview-3gDOjDymlE5d" class="markdown-toolbar-preview" title="Reposition markdown preview" data-aria-label="Reposition markdown preview" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Reposition markdown preview">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$--><g id="markdown-preview-below">
  <rect width="20" height="18" x="2" y="2" rx="2" ry="2" style="fill:none;stroke:var(--colab-icon-color)"></rect>
  <line x1="4.5" y1="13" x2="19.5" y2="13" style="stroke:var(--colab-primary-text-color);stroke-dasharray:2"></line>
  <line x1="2.5" y1="4" x2="21.5" y2="4" style="stroke:var(--colab-icon-color);stroke-width:3px;"></line>
</g></svg></md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!--?--></div></div>
      <div class="editor-container horizontal">
        <div class="editor-root"><div class="editor flex monaco" data-keybinding-context="4" data-mode-id="markdown" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off; display: none;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/24" style="width: 338px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 338px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 332px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 332px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:332px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 332px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">#&nbsp;Setup&nbsp;Environment&nbsp;-&nbsp;Shell/Terminal</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 332px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 276px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 318px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 318px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="29" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 338px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 316px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 338px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 684px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 1 child cell under Setup Environment - Shell/Terminal (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 1 child cell under Setup Environment - Shell/Terminal (Press &lt;Shift&gt; to also collapse sibling sections)" style="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 1 child cell under Setup Environment - Shell/Terminal (Press &lt;Shift&gt; to also collapse sibling sections)">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>Setup Environment - Shell/Terminal</h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Run cell">
        <span class="execution-count"><!--?lit$742065472$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$742065472$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$742065472$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$742065472$--> <!--?lit$742065472$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 1 cell hidden</div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling focused" id="cell-zIK2HSOQlXdB" tabindex="-1" role="region" aria-label="Cell 4: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----> <md-icon-button class="colab-icon" title="Move cell up
Ctrl+M K" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->arrow_upward</md-icon>
            <!--?lit$742065472$-->
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!----> <md-icon-button class="colab-icon" title="Move cell down
Ctrl+M J" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->arrow_downward</md-icon>
            <!--?lit$742065472$-->
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!----> <md-icon-button class="colab-icon" title="Copy link to cell" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->link</md-icon>
            <!--?lit$742065472$-->
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!----> <md-icon-button class="colab-icon" title="Add a comment
Ctrl+Alt+M" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->comment</md-icon>
            <!--?lit$742065472$-->
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!----> <md-icon-button class="colab-icon" title="Open editor settings" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->settings</md-icon>
            <!--?lit$742065472$-->
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!----> <md-icon-button class="colab-icon" title="Edit" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->edit</md-icon>
            <!--?lit$742065472$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->edit_off</md-icon>
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!----> <md-icon-button class="colab-icon" title="Mirror cell in tab" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
            <!--?lit$742065472$-->
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!----> <md-icon-button class="colab-icon" title="Delete cell
Ctrl+M D" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->delete</md-icon>
            <!--?lit$742065472$-->
          </md-icon-button>
          <!--?lit$742065472$--><!--?--><!----><!--?lit$742065472$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More cell actions" data-aria-label="More cell actions" class="colab-icon cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale focused">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell">
        <span class="execution-count"><!--?lit$742065472$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$742065472$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$742065472$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$742065472$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$742065472$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$742065472$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="5" data-mode-id="notebook-python" style="height: 105px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/25" style="width: 627px; height: 105px;"><div data-mprt="3" class="overflow-guard" style="width: 627px; height: 105px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 105px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 105px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 105px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 621px; height: 105px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 105px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 621px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:0px;width:38px;height:19px;"></div><div class="cdr squiggly-warning" style="left:46px;width:54px;height:19px;"></div><div class="cdr squiggly-warning" style="left:108px;width:69px;height:19px;"></div><div class="cdr squiggly-error" style="left:46px;width:54px;height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="current-line" style="width:621px; height:19px;"></div><div class="cdr squiggly-warning" style="left:0px;width:15px;height:19px;"></div><div class="cdr squiggly-warning" style="left:23px;width:54px;height:19px;"></div><div class="cdr squiggly-warning" style="left:85px;width:69px;height:19px;"></div><div class="cdr squiggly-error" style="left:23px;width:54px;height:19px;"></div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:0px;width:46px;height:19px;"></div><div class="cdr squiggly-warning" style="left:54px;width:54px;height:19px;"></div><div class="cdr squiggly-error" style="left:54px;width:54px;height:19px;"></div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:0px;width:46px;height:19px;"></div><div class="cdr squiggly-warning" style="left:54px;width:38px;height:19px;"></div><div class="cdr squiggly-error" style="left:54px;width:38px;height:19px;"></div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="cdr squiggly-warning" style="left:0px;width:23px;height:19px;"></div><div class="cdr squiggly-warning" style="left:31px;width:54px;height:19px;"></div><div class="cdr squiggly-warning" style="left:100px;width:8px;height:19px;"></div><div class="cdr squiggly-warning" style="left:115px;width:92px;height:19px;"></div><div class="cdr squiggly-error" style="left:31px;width:54px;height:19px;"></div><div class="cdr squiggly-error" style="left:115px;width:92px;height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 621px; height: 105px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk1">mkdir&nbsp;project-structure</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1">cd&nbsp;project-structure</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">pipenv&nbsp;install</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">pipenv&nbsp;shell</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">pip&nbsp;install&nbsp;-r&nbsp;requirements.txt</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 621px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 19px; left: 153px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 607px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 607px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="105" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 105px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 105px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 105px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 627px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 19px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 627px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 105px;"><div class="minimap-shadow-hidden" style="height: 105px;"></div><canvas width="0" height="105" style="position: absolute; left: 0px; width: 0px; height: 105px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="105" style="position: absolute; left: 0px; width: 0px; height: 105px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 684px; top: 493.781px; left: 261px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal disabled" style="top: 8px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 0px; height: 0px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px; width: 0px; height: 0px;"><div class="hover-row"><div class="marker hover-contents" style="font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px;"><span style="white-space: pre-wrap;">"structure" is not defined</span><span style="opacity: 0.6; padding-left: 6px;">(reportUndefinedVariable)</span></div></div><div class="hover-row markdown-hover"><div class="hover-contents code-hover-contents"><div class="rendered-markdown"><div data-code="id#12"><span style="font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px;"><div class="monaco-tokenized-source"><span class="mtk1">structure: Any</span></div></span></div></div></div></div><div class="hover-row status-bar"><div class="actions"><div class="action-container" tabindex="0"><a class="action" role="button"><span>View Problem (Alt+F8)</span></a></div><div>No quick fixes available</div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 0px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 0px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 0px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 4 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> <div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div></div><div class="cell text" id="cell-KvDWS5NLleKJ" tabindex="-1" role="region" aria-label="Cell 5: Text cell: Run Streamlit app" style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"><div class="markdown-toolbar"><!----><!--?lit$742065472$--><!----><md-icon-button id="markdown-toolbar-header-KvDWS5NLleKJ" class="markdown-toolbar-header" title="Toggle heading" data-aria-label="Toggle heading" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle heading">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_size</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-bold-KvDWS5NLleKJ" class="markdown-toolbar-bold" title="Bold" data-aria-label="Bold" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Bold">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_bold</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-italic-KvDWS5NLleKJ" class="markdown-toolbar-italic" title="Italicise" data-aria-label="Italicise" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Italicise">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_italic</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-code-KvDWS5NLleKJ" class="markdown-toolbar-code" title="Format as code" data-aria-label="Format as code" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Format as code">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->code</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-link-KvDWS5NLleKJ" class="markdown-toolbar-link" title="Insert link" data-aria-label="Insert link" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert link">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->link</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><label for="markdown-image-input-KvDWS5NLleKJ" class="colab-icon markdown-toolbar-insert-image">
        <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <span role="button" tabindex="0" id="markdown-toolbar-insert-image-KvDWS5NLleKJ" title="Insert image" aria-label="Insert image">
          <md-focus-ring aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>image</md-icon>
        </span>
        <!--?lit$742065472$-->
      </label>
      <input class="markdown-image-input" type="file" multiple="" accept="image/*" id="markdown-image-input-KvDWS5NLleKJ"><!----><!----><md-icon-button id="markdown-toolbar-blockquote-KvDWS5NLleKJ" class="markdown-toolbar-blockquote" title="Add blockquote" data-aria-label="Add blockquote" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add blockquote">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_quote</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ol-KvDWS5NLleKJ" class="markdown-toolbar-ol" title="Add numbered list" data-aria-label="Add numbered list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add numbered list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_numbered</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-ul-KvDWS5NLleKJ" class="markdown-toolbar-ul" title="Add bulleted list" data-aria-label="Add bulleted list" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add bulleted list">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->format_list_bulleted</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-hr-KvDWS5NLleKJ" class="markdown-toolbar-hr" title="Add horizontal rule" data-aria-label="Add horizontal rule" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add horizontal rule">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->horizontal_rule</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-latex-KvDWS5NLleKJ" class="markdown-toolbar-latex" title="LaTeX" data-aria-label="LaTeX" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="LaTeX">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><span aria-hidden="true">ψ</span>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-emoji-KvDWS5NLleKJ" class="markdown-toolbar-emoji" title="Insert emoji" data-aria-label="Insert emoji" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Insert emoji">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->mood</md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!----><md-icon-button id="markdown-toolbar-preview-KvDWS5NLleKJ" class="markdown-toolbar-preview" title="Reposition markdown preview" data-aria-label="Reposition markdown preview" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Reposition markdown preview">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <!--?lit$742065472$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$--><g id="markdown-preview-below">
  <rect width="20" height="18" x="2" y="2" rx="2" ry="2" style="fill:none;stroke:var(--colab-icon-color)"></rect>
  <line x1="4.5" y1="13" x2="19.5" y2="13" style="stroke:var(--colab-primary-text-color);stroke-dasharray:2"></line>
  <line x1="2.5" y1="4" x2="21.5" y2="4" style="stroke:var(--colab-icon-color);stroke-width:3px;"></line>
</g></svg></md-icon>
      </md-icon-button>
      <!--?lit$742065472$--><!--?--><!----><!--?--></div></div>
      <div class="editor-container horizontal">
        <div class="editor-root"><div class="editor flex monaco" data-keybinding-context="6" data-mode-id="markdown" style="height: 29px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off; display: none;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/26" style="width: 338px; height: 29px;"><div data-mprt="3" class="overflow-guard" style="width: 338px; height: 29px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 29px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 29px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 29px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 332px; height: 29px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 29px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 332px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="cslr selected-text top-left-radius bottom-left-radius top-right-radius bottom-right-radius" style="top:0px;left:15px;width:131px;height:19px;"></div><svg style="position:absolute;width:123px;height:19px" viewBox="0 0 123 19" xmlns="http://www.w3.org/2000/svg" fill="rgba(51, 51, 51, 0.2)"><circle cx="41.85" cy="9.50" r="1.10"></circle><circle cx="118.85" cy="9.50" r="1.10"></circle></svg></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 332px; height: 29px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk6">#&nbsp;Run&nbsp;Streamlit&nbsp;app</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 332px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer has-selection cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 145px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 318px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 318px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="29" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 29px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 29px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 29px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 338px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 316px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 338px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 29px;"><div class="minimap-shadow-hidden" style="height: 29px;"></div><canvas width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="29" style="position: absolute; left: 0px; width: 0px; height: 29px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 684px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 500px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 1 child cell under Run Streamlit app (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 1 child cell under Run Streamlit app (Press &lt;Shift&gt; to also collapse sibling sections)" style="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 1 child cell under Run Streamlit app (Press &lt;Shift&gt; to also collapse sibling sections)">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>Run Streamlit app</h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Run cell">
        <span class="execution-count"><!--?lit$742065472$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$742065472$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$742065472$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$742065472$--> <!--?lit$742065472$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 1 cell hidden</div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div></div><div class="cell code icon-scrolling" id="cell-3k5hazoZlhq3" tabindex="-1" role="region" aria-label="Cell 6: Code cell: " style="opacity: 1;"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell">
        <span class="execution-count"><!--?lit$742065472$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$742065472$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$742065472$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$742065472$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$742065472$--><!----><div><!--?lit$742065472$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$742065472$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$742065472$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab colab colab colab colab" data-lang="notebook-python"><span><span class="mtk1">streamlit&nbsp;run&nbsp;dashboard.py</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$742065472$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 6 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> <div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$742065472$-->Text
        </md-outlined-button>
        <!--?lit$742065472$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$742065472$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$742065472$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$742065472$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style=""></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$742065472$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$742065472$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$742065472$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$742065472$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$742065472$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$742065472$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$742065472$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./README_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./README_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" style="min-height: inherit;"><template shadowrootmode="open"><!----> <!--?lit$742065472$--> <div class="connect-status">
        <md-icon status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$--><svg viewBox="0 0 24 24"><!--?lit$742065472$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
        <div aria-atomic="true" aria-live="polite"><!--?lit$742065472$-->Connected to Python 3 Google Compute Engine backend</div>
      </div>
      <md-icon-button class="visible-on-closed" title="Connected" disabled="" value="" data-aria-label="Connected"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Connected" disabled="">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$742065472$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <!--?lit$742065472$-->
      <md-icon-button title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$742065472$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$742065472$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$742065472$--><span class="icon"><slot></slot></span>
        <!--?lit$742065472$-->
        <!--?lit$742065472$--><span class="touch"></span>
        <!--?lit$742065472$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="locate-in-drive" class="goog-menuitem " role="menuitem" id=":33" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Locate in Drive<!--?lit$742065472$--></div></div><div command="open-in-playground" class="goog-menuitem " role="menuitem" id=":34" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Open in playground mode<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":35" style="user-select: none;"></div><div command="new" class="goog-menuitem " role="menuitem" id=":36" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->New notebook in Drive<!--?lit$742065472$--></div></div><div command="open" class="goog-menuitem " role="menuitem" id=":37" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Open notebook<!--?lit$742065472$--></div></div><div command="import-notebook" class="goog-menuitem " role="menuitem" id=":38" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Upload notebook<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":39" style="user-select: none;"></div><div command="rename" class="goog-menuitem " role="menuitem" id=":3a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Rename<!--?lit$742065472$--></div></div><div command="move-notebook" class="goog-menuitem " role="menuitem" id=":3b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Move<!--?lit$742065472$--></div></div><div command="trash" class="goog-menuitem " role="menuitem" id=":3c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Move to the bin<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3d" style="user-select: none;"></div><div command="clone" class="goog-menuitem " role="menuitem" id=":3e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Save a copy in Drive<!--?lit$742065472$--></div></div><div command="copy-to-gist" class="goog-menuitem " role="menuitem" id=":3f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Save a copy as a GitHub Gist<!--?lit$742065472$--></div></div><div command="copy-to-github" class="goog-menuitem " role="menuitem" id=":3g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Save a copy in GitHub<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3h" style="user-select: none;"></div><div command="save" class="goog-menuitem " role="menuitem" id=":3i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Save<!--?lit$742065472$--></div></div><div command="save-and-checkpoint" class="goog-menuitem " role="menuitem" id=":3j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Save and pin revision<!--?lit$742065472$--></div></div><div command="show-history" class="goog-menuitem " role="menuitem" id=":3k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Revision history<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3l" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$742065472$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class="goog-menuitem " role="menuitem" id=":3p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Print<!--?lit$742065472$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="download-ipynb" class="goog-menuitem " role="menuitem" id=":3n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Download .ipynb<!--?lit$742065472$--></div></div><div command="download-python" class="goog-menuitem " role="menuitem" id=":3o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Download .py<!--?lit$742065472$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="undo" class="goog-menuitem " role="menuitem" id=":3r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Undo<!--?lit$742065472$--></div></div><div command="redo" class="goog-menuitem " role="menuitem" id=":3s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Redo<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3t" style="user-select: none;"></div><div command="select-all" class="goog-menuitem " role="menuitem" id=":3u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Select all cells<!--?lit$742065472$--></div></div><div command="cut" class="goog-menuitem " role="menuitem" id=":3v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Cut cell or selection<!--?lit$742065472$--></div></div><div command="copy" class="goog-menuitem " role="menuitem" id=":3w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Copy cell or selection<!--?lit$742065472$--></div></div><div command="paste" class="goog-menuitem " role="menuitem" id=":3x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Paste<!--?lit$742065472$--></div></div><div command="delete-cell-or-selection" class="goog-menuitem " role="menuitem" id=":3y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Delete selected cells<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3z" style="user-select: none;"></div><div command="find" class="goog-menuitem " role="menuitem" id=":40" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Find and replace<!--?lit$742065472$--></div></div><div command="find-next" class="goog-menuitem " role="menuitem" id=":41" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Find next<!--?lit$742065472$--></div></div><div command="find-previous" class="goog-menuitem " role="menuitem" id=":42" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Find previous<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":43" style="user-select: none;"></div><div command="notebook-settings" class="goog-menuitem " role="menuitem" id=":44" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Notebook settings<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":45" style="user-select: none;"></div><div command="clear-outputs" class="goog-menuitem " role="menuitem" id=":46" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Clear all outputs<!--?lit$742065472$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":48" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$742065472$-->Table of contents<!--?lit$742065472$--></div></div><div command="show-fileinfo" class="goog-menuitem " role="menuitem" id=":49" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Notebook info<!--?lit$742065472$--></div></div><div command="show-executedcode" class="goog-menuitem " role="menuitem" id=":4a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Executed code history<!--?lit$742065472$--></div></div><div command="toggle-comments-visibility" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":4b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$742065472$-->Comments sidebar<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4c" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem " role="menuitem" id=":4d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Collapse sections<!--?lit$742065472$--></div></div><div command="expand-sections" class="goog-menuitem " role="menuitem" id=":4e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Expand sections<!--?lit$742065472$--></div></div><div command="save-section-layout" class="goog-menuitem " role="menuitem" id=":4f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Save collapsed section layout<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4g" style="user-select: none;"></div><div command="hide-code" class="goog-menuitem " role="menuitem" id=":4h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Show/hide code<!--?lit$742065472$--></div></div><div command="toggle-output" class="goog-menuitem " role="menuitem" id=":4i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Show/hide output<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4j" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem " role="menuitem" id=":4k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Focus next tab<!--?lit$742065472$--></div></div><div command="focus-previous-tab" class="goog-menuitem " role="menuitem" id=":4l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Focus previous tab<!--?lit$742065472$--></div></div><div command="move-tab-to-next" class="goog-menuitem " role="menuitem" id=":4m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Move tab to next pane<!--?lit$742065472$--></div></div><div command="move-tab-to-prev" class="goog-menuitem " role="menuitem" id=":4n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Move tab to previous pane<!--?lit$742065472$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="insert-cell-below" class="goog-menuitem " role="menuitem" id=":4p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Code cell<!--?lit$742065472$--></div></div><div command="add-text" class="goog-menuitem " role="menuitem" id=":4q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Text cell<!--?lit$742065472$--></div></div><div command="add-section-header" class="goog-menuitem " role="menuitem" id=":4r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Section header cell<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4s" style="user-select: none;"></div><div command="open-scratch-code-cell" class="goog-menuitem " role="menuitem" id=":4t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Scratch code cell<!--?lit$742065472$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":4u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Code snippets<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4v" style="user-select: none;"></div><div command="add-form-field" class="goog-menuitem " role="menuitem" id=":4w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Add a form field<!--?lit$742065472$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="runall" class="goog-menuitem " role="menuitem" id=":4y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Run all<!--?lit$742065472$--></div></div><div command="runbefore" class="goog-menuitem " role="menuitem" id=":4z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Run before<!--?lit$742065472$--></div></div><div command="runfocused" class="goog-menuitem " role="menuitem" id=":50" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Run the focused cell<!--?lit$742065472$--></div></div><div command="runselected" class="goog-menuitem " role="menuitem" id=":51" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Run selection<!--?lit$742065472$--></div></div><div command="runafter" class="goog-menuitem " role="menuitem" id=":52" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Run after<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":53" style="user-select: none;"></div><div command="interrupt" class="goog-menuitem " role="menuitem" id=":54" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Interrupt execution<!--?lit$742065472$--></div></div><div command="restart" class="goog-menuitem " role="menuitem" id=":55" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Restart session<!--?lit$742065472$--></div></div><div command="restart-and-run-all" class="goog-menuitem " role="menuitem" id=":56" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Restart session and run all<!--?lit$742065472$--></div></div><div command="powerwash-current-vm" class="goog-menuitem " role="menuitem" id=":57" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Disconnect and delete runtime<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":58" style="user-select: none;"></div><div command="change-runtime-type" class="goog-menuitem " role="menuitem" id=":59" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Change runtime type<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5a" style="user-select: none;"></div><div command="manage-sessions" class="goog-menuitem " role="menuitem" id=":5b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Manage sessions<!--?lit$742065472$--></div></div><div command="open-resource-viewer" class="goog-menuitem " role="menuitem" id=":5c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->View resources<!--?lit$742065472$--></div></div><div command="view-runtime-logs" class="goog-menuitem " role="menuitem" id=":5d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->View runtime logs<!--?lit$742065472$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="show-command-palette" class="goog-menuitem " role="menuitem" id=":5f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Command palette<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5g" style="user-select: none;"></div><div command="preferences" class="goog-menuitem " role="menuitem" id=":5h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Settings<!--?lit$742065472$--></div></div><div command="shortcuts" class="goog-menuitem " role="menuitem" id=":5i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Keyboard shortcuts<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5j" style="user-select: none;"></div><div command="open-differ" class="goog-menuitem " role="menuitem" id=":5k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Diff notebooks<!--?lit$742065472$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$742065472$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$742065472$--><div command="faq" class="goog-menuitem " role="menuitem" id=":5m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Frequently asked questions<!--?lit$742065472$--></div></div><div command="view-relnotes" class="goog-menuitem " role="menuitem" id=":5n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->View release notes<!--?lit$742065472$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":5o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Search code snippets<!--?lit$742065472$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5p" style="user-select: none;"></div><div command="report-bug" class="goog-menuitem " role="menuitem" id=":5q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Report a bug<!--?lit$742065472$--></div></div><div command="report-abuse" class="goog-menuitem " role="menuitem" id=":5r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Report Drive abuse<!--?lit$742065472$--></div></div><div command="send-feedback" class="goog-menuitem " role="menuitem" id=":5s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->Send feedback<!--?lit$742065472$--></div></div><div command="view-tos" class="goog-menuitem " role="menuitem" id=":5t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->View Terms of Service<!--?lit$742065472$--></div></div><div command="view-in-english" class="goog-menuitem " role="menuitem" id=":5u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$742065472$-->View in English<!--?lit$742065472$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$742065472$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$742065472$--><button id="button" class="button">
      <!--?lit$742065472$-->
      <span class="touch"></span>
      <!--?lit$742065472$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$742065472$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$742065472$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;">avg_transaction_per_customer = avg_transaction_per_customer.sort_values(by='avg_payment_value', ascending=False)</div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><div><div class="grecaptcha-badge" data-style="none" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-13n9b7rjrjga" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./README_files/anchor(1).html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100001" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div></div></body><grammarly-desktop-integration data-grammarly-shadow-root="true"><template shadowrootmode="open"><style>
      div.grammarly-desktop-integration {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select:none;
        user-select:none;
      }

      div.grammarly-desktop-integration:before {
        content: attr(data-content);
      }
    </style><div aria-label="grammarly-integration" role="group" tabindex="-1" class="grammarly-desktop-integration" data-content="{&quot;mode&quot;:&quot;full&quot;,&quot;isActive&quot;:true,&quot;isUserDisabled&quot;:false}"></div></template></grammarly-desktop-integration></html>