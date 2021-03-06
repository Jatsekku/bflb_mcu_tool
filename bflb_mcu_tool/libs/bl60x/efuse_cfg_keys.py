# -*- coding:utf-8 -*-


efuse_cfg_keys = {
    "ef_sf_aes_mode": {
        "offset": "0",
        "pos": "0",
        "bitlen": "2"
    },
    "ef_sboot_sign_mode": {
        "offset": "0",
        "pos": "2",
        "bitlen": "2"
    },
    "ef_sboot_en": {
        "offset": "0",
        "pos": "4",
        "bitlen": "4"
    },
    "ef_sw_cam_dis": {
        "offset": "0",
        "pos": "14",
        "bitlen": "1"
    },
    "ef_sw_sf_dis": {
        "offset": "0",
        "pos": "15",
        "bitlen": "1"
    },
    "ef_mac_dbg_dis": {
        "offset": "0",
        "pos": "16",
        "bitlen": "2"
    },
    "ef_cpu_rst_dbg_dis": {
        "offset": "0",
        "pos": "18",
        "bitlen": "2"
    },
    "ef_sf_dbg_dis": {
        "offset": "0",
        "pos": "20",
        "bitlen": "2"
    },
    "ef_se_dbg_dis": {
        "offset": "0",
        "pos": "22",
        "bitlen": "2"
    },
    "ef_efuse_dbg_dis": {
        "offset": "0",
        "pos": "24",
        "bitlen": "2"
    },
    "ef_dbg_jtag_dis": {
        "offset": "0",
        "pos": "26",
        "bitlen": "2"
    },
    "ef_dbg_mode": {
        "offset": "0",
        "pos": "28",
        "bitlen": "4"
    },
    "ef_dbg_pwd_low": {
        "offset": "4",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_dbg_pwd_high": {
        "offset": "8",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_chip_id_low": {
        "offset": "12",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_chip_id_high": {
        "offset": "16",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_wifi_mac_low": {
        "offset": "20",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_wifi_mac_high": {
        "offset": "24",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_flash_psram_info": {
        "offset": "24",
        "pos": "27",
        "bitlen": "2"
    },
    "ef_core_info": {
        "offset": "24",
        "pos": "29",
        "bitlen": "1"
    },
    "ef_wifi_mcu_info": {
        "offset": "24",
        "pos": "30",
        "bitlen": "1"
    },
    "ef_pack_info": {
        "offset": "24",
        "pos": "31",
        "bitlen": "1"
    },
    "ef_key_slot_0_w0": {
        "offset": "28",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_0_w1": {
        "offset": "32",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_0_w2": {
        "offset": "36",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_0_w3": {
        "offset": "40",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_1_w0": {
        "offset": "44",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_1_w1": {
        "offset": "48",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_1_w2": {
        "offset": "52",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_1_w3": {
        "offset": "56",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_2_w0": {
        "offset": "60",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_2_w1": {
        "offset": "64",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_2_w2": {
        "offset": "68",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_2_w3": {
        "offset": "72",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_3_w0": {
        "offset": "76",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_3_w1": {
        "offset": "80",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_3_w2": {
        "offset": "84",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_3_w3": {
        "offset": "88",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_4_w0": {
        "offset": "92",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_4_w1": {
        "offset": "96",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_4_w2": {
        "offset": "100",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_4_w3": {
        "offset": "104",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_5_w0": {
        "offset": "108",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_5_w1": {
        "offset": "112",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_5_w2": {
        "offset": "116",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_5_w3": {
        "offset": "120",
        "pos": "0",
        "bitlen": "32"
    },
    "wr_lock_sboot_sign_mode": {
        "offset": "124",
        "pos": "5",
        "bitlen": "1"
    },
    "wr_lock_sf_aes_mode": {
        "offset": "124",
        "pos": "6",
        "bitlen": "1"
    },
    "wr_lock_dbg_pwd": {
        "offset": "124",
        "pos": "7",
        "bitlen": "1"
    },
    "wr_lock_chip_id": {
        "offset": "124",
        "pos": "8",
        "bitlen": "1"
    },
    "wr_lock_wifi_mac": {
        "offset": "124",
        "pos": "9",
        "bitlen": "1"
    },
    "wr_lock_key_slot_0": {
        "offset": "124",
        "pos": "10",
        "bitlen": "1"
    },
    "wr_lock_key_slot_1": {
        "offset": "124",
        "pos": "11",
        "bitlen": "1"
    },
    "wr_lock_key_slot_2": {
        "offset": "124",
        "pos": "12",
        "bitlen": "1"
    },
    "wr_lock_key_slot_3": {
        "offset": "124",
        "pos": "13",
        "bitlen": "1"
    },
    "wr_lock_key_slot_4": {
        "offset": "124",
        "pos": "14",
        "bitlen": "1"
    },
    "wr_lock_key_slot_5": {
        "offset": "124",
        "pos": "15",
        "bitlen": "1"
    },
    "rd_lock_dbg_pwd": {
        "offset": "124",
        "pos": "23",
        "bitlen": "1"
    },
    "rd_lock_key_slot_0": {
        "offset": "124",
        "pos": "26",
        "bitlen": "1"
    },
    "rd_lock_key_slot_1": {
        "offset": "124",
        "pos": "27",
        "bitlen": "1"
    },
    "rd_lock_key_slot_2": {
        "offset": "124",
        "pos": "28",
        "bitlen": "1"
    },
    "rd_lock_key_slot_3": {
        "offset": "124",
        "pos": "29",
        "bitlen": "1"
    },
    "rd_lock_key_slot_4": {
        "offset": "124",
        "pos": "30",
        "bitlen": "1"
    },
    "rd_lock_key_slot_5": {
        "offset": "124",
        "pos": "31",
        "bitlen": "1"
    },
    "ef_ana_trim_0": {
        "offset": "128",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_ana_trim_1": {
        "offset": "132",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_ana_trim_2": {
        "offset": "136",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_sw_usage_0": {
        "offset": "140",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_sw_usage_1": {
        "offset": "144",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_sw_usage_2": {
        "offset": "148",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_sw_usage_3": {
        "offset": "152",
        "pos": "0",
        "bitlen": "32"
    },
    ###################################################################
    "bootrom_protect": {
        "offset": "140",
        "pos": "0",
        "bitlen": "1"
    },
    "uart_disable": {
        "offset": "140",
        "pos": "1",
        "bitlen": "1"
    },
    "sdio_pin_sel": {
        "offset": "140",
        "pos": "2",
        "bitlen": "1"
    },
    "jtag_switch": {
        "offset": "140",
        "pos": "3",
        "bitlen": "1"
    },
    "tz_boot": {
        "offset": "140",
        "pos": "4",
        "bitlen": "1"
    },
    "encryped_with_sign": {
        "offset": "140",
        "pos": "5",
        "bitlen": "1"
    },
    "external_flash": {
        "offset": "140",
        "pos": "6",
        "bitlen": "2"
    },
    "xtal_type": {
        "offset": "140",
        "pos": "8",
        "bitlen": "3"
    },
    "pll_clk": {
        "offset": "140",
        "pos": "11",
        "bitlen": "2"
    },
    "hclk_div": {
        "offset": "140",
        "pos": "13",
        "bitlen": "1"
    },
    "bclk_div": {
        "offset": "140",
        "pos": "14",
        "bitlen": "1"
    },
    "uart_fix_bdr": {
        "offset": "140",
        "pos": "15",
        "bitlen": "1"
    },
    "flash_clk_type": {
        "offset": "140",
        "pos": "16",
        "bitlen": "3"
    },
    "flash_pwr_delay0": {
        "offset": "140",
        "pos": "19",
        "bitlen": "1"
    },
    "hbn_check_sign": {
        "offset": "140",
        "pos": "20",
        "bitlen": "1"
    },
    "mediaboot_disable": {
        "offset": "140",
        "pos": "21",
        "bitlen": "1"
    },
    "uartboot_disable": {
        "offset": "140",
        "pos": "22",
        "bitlen": "1"
    },
    "sdioboot_disable": {
        "offset": "140",
        "pos": "23",
        "bitlen": "1"
    },
    "keep_dbg_port_closed": {
        "offset": "140",
        "pos": "24",
        "bitlen": "1"
    },
    "vddio_18_user_ctrl": {
        "offset": "140",
        "pos": "25",
        "bitlen": "1"
    },
    "vddio_18_sw1": {
        "offset": "140",
        "pos": "26",
        "bitlen": "1"
    },
    "vddio_18_sw2": {
        "offset": "140",
        "pos": "27",
        "bitlen": "1"
    },
    "vddio_18_sw3": {
        "offset": "140",
        "pos": "28",
        "bitlen": "1"
    },
    "vddio_18_bypass": {
        "offset": "140",
        "pos": "29",
        "bitlen": "1"
    },
    "vddio_18_repower": {
        "offset": "140",
        "pos": "30",
        "bitlen": "1"
    },
    "flash_pwr_delay1": {
        "offset": "140",
        "pos": "31",
        "bitlen": "1"
    },
    ############################################## ###########################
    "ef_key_slot_6_w0": {
        "offset": "156",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_6_w1": {
        "offset": "160",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_6_w2": {
        "offset": "164",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_6_w3": {
        "offset": "168",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_7_w0": {
        "offset": "172",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_7_w1": {
        "offset": "176",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_7_w2": {
        "offset": "180",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_7_w3": {
        "offset": "184",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_8_w0": {
        "offset": "188",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_8_w1": {
        "offset": "192",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_8_w2": {
        "offset": "196",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_8_w3": {
        "offset": "200",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_9_w0": {
        "offset": "204",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_9_w1": {
        "offset": "208",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_9_w2": {
        "offset": "212",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_9_w3": {
        "offset": "216",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_10_w0": {
        "offset": "220",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_10_w1": {
        "offset": "224",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_10_w2": {
        "offset": "228",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_10_w3": {
        "offset": "232",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_11_w0": {
        "offset": "236",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_11_w1": {
        "offset": "240",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_11_w2": {
        "offset": "244",
        "pos": "0",
        "bitlen": "32"
    },
    "ef_key_slot_11_w3": {
        "offset": "248",
        "pos": "0",
        "bitlen": "32"
    },
    "wr_lock_ana_trim_0": {
        "offset": "252",
        "pos": "3",
        "bitlen": "1"
    },
    "wr_lock_ana_trim_1": {
        "offset": "252",
        "pos": "4",
        "bitlen": "1"
    },
    "wr_lock_ana_trim_2": {
        "offset": "252",
        "pos": "5",
        "bitlen": "1"
    },
    "wr_lock_sw_usage_0": {
        "offset": "252",
        "pos": "6",
        "bitlen": "1"
    },
    "wr_lock_sw_usage_1": {
        "offset": "252",
        "pos": "7",
        "bitlen": "1"
    },
    "wr_lock_sw_usage_2": {
        "offset": "252",
        "pos": "8",
        "bitlen": "1"
    },
    "wr_lock_sw_usage_3": {
        "offset": "252",
        "pos": "9",
        "bitlen": "1"
    },
    "wr_lock_key_slot_6": {
        "offset": "252",
        "pos": "10",
        "bitlen": "1"
    },
    "wr_lock_key_slot_7": {
        "offset": "252",
        "pos": "11",
        "bitlen": "1"
    },
    "wr_lock_key_slot_8": {
        "offset": "252",
        "pos": "12",
        "bitlen": "1"
    },
    "wr_lock_key_slot_9": {
        "offset": "252",
        "pos": "13",
        "bitlen": "1"
    },
    "wr_lock_key_slot_10": {
        "offset": "252",
        "pos": "14",
        "bitlen": "1"
    },
    "wr_lock_key_slot_11": {
        "offset": "252",
        "pos": "15",
        "bitlen": "1"
    },
    "rd_lock_key_slot_6": {
        "offset": "252",
        "pos": "26",
        "bitlen": "1"
    },
    "rd_lock_key_slot_7": {
        "offset": "252",
        "pos": "27",
        "bitlen": "1"
    },
    "rd_lock_key_slot_8": {
        "offset": "252",
        "pos": "28",
        "bitlen": "1"
    },
    "rd_lock_key_slot_9": {
        "offset": "252",
        "pos": "29",
        "bitlen": "1"
    },
    "rd_lock_key_slot_10": {
        "offset": "252",
        "pos": "30",
        "bitlen": "1"
    },
    "rd_lock_key_slot_11": {
        "offset": "252",
        "pos": "31",
        "bitlen": "1"
    },
}

efuse_mac_slot_offset = {
    "slot0": "20",
    "slot1": "12",
    "slot2": "204",
}
