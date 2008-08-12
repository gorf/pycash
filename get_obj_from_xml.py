def get_objects(xml):
   #get widget from XML
   win_main = xml.get_widget('win_main')
   win_about = xml.get_widget('win_about')
   win_trading = xml.get_widget('win_trading')
   win_msg = xml.get_widget('win_msg')
   win_boss_come = xml.get_widget('win_boss_come')
   win_post_office = xml.get_widget('win_post_office')
   
   m_start = xml.get_widget('m_start')
   m_create_book = xml.get_widget('m_create_book')
   m_open_book = xml.get_widget('m_open_book')
   m_rich = xml.get_widget('m_rich')
   m_exit = xml.get_widget('m_exit')
   m_about = xml.get_widget('m_about')
   
   l_trading = xml.get_widget('l_trading')
   spb_trading = xml.get_widget('spb_trading')
   b_trading_cancel = xml.get_widget('b_trading_cancel')
   b_trading_ok = xml.get_widget('b_trading_ok')
   b_add_account = xml.get_widget('b_add_account')
   
   b_about = xml.get_widget('b_about')
   
   l_msg = xml.get_widget('l_msg')
   b_msg = xml.get_widget('b_msg')
   
   tview_all_account = xml.get_widget('tview_all_account')
   tview_register = xml.get_widget('tview_register')
   b_buy = xml.get_widget('b_buy')
   b_sell = xml.get_widget('b_sell')
   b_boss_come = xml.get_widget('b_boss_come')
   
   et_cash = xml.get_widget('et_cash')
   et_debt = xml.get_widget('et_debt')
   et_fund = xml.get_widget('et_fund')
   et_lend = xml.get_widget('et_lend')
   et_health = xml.get_widget('et_health')
   et_repute = xml.get_widget('et_repute')
   
   b_gb_dxsc = xml.get_widget('b_gb_dxsc')
   b_gb_lhl = xml.get_widget('b_gb_lhl')
   b_gb_wjbh = xml.get_widget('b_gb_wjbh')
   b_gb_ybbh = xml.get_widget('b_gb_ybbh')
   b_gb_gsj = xml.get_widget('b_gb_gsj')
   b_gb_ybbl = xml.get_widget('b_gb_ybbl')
   b_gb_yhd = xml.get_widget('b_gb_yhd')
   b_gb_xw = xml.get_widget('b_gb_xw')
   
   b_jd_jzc = xml.get_widget('b_jd_jzc')
   b_jd_hbyc = xml.get_widget('b_jd_hbyc')
   b_jd_hbgy = xml.get_widget('b_jd_hbgy')
   b_jd_ghzx = xml.get_widget('b_jd_ghzx')
   b_jd_jzg = xml.get_widget('b_jd_jzg')
   b_jd_tlwbh = xml.get_widget('b_jd_tlwbh')
   b_jd_zyy = xml.get_widget('b_jd_zyy')
   b_jd_nyjd = xml.get_widget('b_jd_nyjd')
   
   b_xz_wzs = xml.get_widget('b_xz_wzs')
   b_xz_qs = xml.get_widget('b_xz_qs')
   b_xz_szf = xml.get_widget('b_xz_szf')
   b_xz_djs = xml.get_widget('b_xz_djs')
   b_xz_tyzx = xml.get_widget('b_xz_tyzx')
   b_xz_nx = xml.get_widget('b_xz_nx')
   b_xz_zdwy = xml.get_widget('b_xz_zdwy')
   b_xz_888j = xml.get_widget('b_xz_888j')
   b_xz_gmj = xml.get_widget('b_xz_gmj')
   
   b_tj_mlw = xml.get_widget('b_tj_mlw')
   b_tj_js = xml.get_widget('b_tj_js')
   b_tj_qhkjy = xml.get_widget('b_tj_qhkjy')
   b_tj_zsdx = xml.get_widget('b_tj_zsdx')
   b_tj_tjsc = xml.get_widget('b_tj_tjsc')
   b_tj_nfrjy = xml.get_widget('b_tj_nfrjy')
   b_tj_hgd = xml.get_widget('b_tj_hgd')
   b_tj_gjscc = xml.get_widget('b_tj_gjscc')
   b_tj_bsd = xml.get_widget('b_tj_bsd')
   b_tj_qad = xml.get_widget('b_tj_qad')
   b_tj_jd = xml.get_widget('b_tj_jd')
      
   b_np_npsc = xml.get_widget('b_np_npsc')
   b_np_hq = xml.get_widget('b_np_hq')
   b_np_npgyy = xml.get_widget('b_np_npgyy')
   b_np_zxd = xml.get_widget('b_np_zxd')
   b_np_dm = xml.get_widget('b_np_dm')
   b_np_sz = xml.get_widget('b_np_sz')
   
   b_post_office = xml.get_widget('b_post_office')
   l_post_office = xml.get_widget('l_post_office')
   spb_post_office = xml.get_widget('spb_post_office')
   b_post_office_ok = xml.get_widget('b_post_office_ok')
   b_post_office_cancel = xml.get_widget('b_post_office_cancel')
   
   all_widget = {
      "win_main":win_main,
      "win_about":win_about,
      "win_trading":win_trading,
      "win_msg":win_msg,
      "win_boss_come":win_boss_come,
      "win_post_office":win_post_office,
      
      "m_start":m_start,
      "m_create_book":m_create_book,
      "m_open_book":m_open_book,
      "m_rich":m_rich,
      "m_exit":m_exit,
      "m_about":m_about,
      
      "l_trading":l_trading,
      "spb_trading":spb_trading,
      "b_trading_cancel":b_trading_cancel,
      "b_trading_ok":b_trading_ok,
      "b_add_account":b_add_account,
      
      "b_about":b_about,
      
      "l_msg":l_msg,
      "b_msg":b_msg,
      
      "tview_all_account":tview_all_account,
      "tview_register":tview_register,
      "b_buy":b_buy,
      "b_sell":b_sell,
      "b_boss_come":b_boss_come,
      
      "et_cash":et_cash,
      "et_debt":et_debt,
      "et_fund":et_fund,
      "et_lend":et_lend,
      "et_health":et_health,
      "et_repute":et_repute,
      
      "b_gb_dxsc":b_gb_dxsc,
      "b_gb_lhl":b_gb_lhl,
      "b_gb_wjbh":b_gb_wjbh,
      "b_gb_ybbh":b_gb_ybbh,
      "b_gb_gsj":b_gb_gsj,
      "b_gb_ybbl":b_gb_ybbl,
      "b_gb_yhd":b_gb_yhd,
      "b_gb_xw":b_gb_xw,
   
      "b_jd_jzc":b_jd_jzc,
      "b_jd_hbyc":b_jd_hbyc,
      "b_jd_hbgy":b_jd_hbgy,
      "b_jd_ghzx":b_jd_ghzx,
      "b_jd_jzg":b_jd_jzg,
      "b_jd_tlwbh":b_jd_tlwbh,
      "b_jd_zyy":b_jd_zyy,
      "b_jd_nyjd":b_jd_nyjd,
   
      "b_xz_wzs":b_xz_wzs,
      "b_xz_qs":b_xz_qs,
      "b_xz_szf":b_xz_szf,
      "b_xz_djs":b_xz_djs,
      "b_xz_tyzx":b_xz_tyzx,
      "b_xz_nx":b_xz_nx,
      "b_xz_zdwy":b_xz_zdwy,
      "b_xz_888j":b_xz_888j,
      "b_xz_gmj":b_xz_gmj,
      
      "b_tj_mlw":b_tj_mlw,
      "b_tj_js":b_tj_js,
      "b_tj_qhkjy":b_tj_qhkjy,
      "b_tj_zsdx":b_tj_zsdx,
      "b_tj_tjsc":b_tj_tjsc,
      "b_tj_nfrjy":b_tj_nfrjy,
      "b_tj_hgd":b_tj_hgd,
      "b_tj_gjscc":b_tj_gjscc,
      "b_tj_bsd":b_tj_bsd,
      "b_tj_qad":b_tj_qad,
      "b_tj_jd":b_tj_jd,
      
      "b_np_npsc":b_np_npsc,
      "b_np_hq":b_np_hq,
      "b_np_npgyy":b_np_npgyy,
      "b_np_zxd":b_np_zxd,
      "b_np_dm":b_np_dm,
      "b_np_sz":b_np_sz,
      
      "b_post_office":b_post_office,
      "l_post_office":l_post_office,
      "spb_post_office":spb_post_office,
      "b_post_office_ok":b_post_office_ok,
      "b_post_office_cancel":b_post_office_cancel,
      
      }
   return all_widget
