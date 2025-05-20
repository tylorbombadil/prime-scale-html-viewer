# Project Architecture Snapshot

## Directory Tree

**.** _(Full Path: `/home/mint/prime-scale-html-viewer`)_

├── `index.html`
├── **output/**
│   ├── `gap_scout_match_5_notes.json`
│   ├── `log_prime_scale_13_valley.json`
│   ├── `log_prime_scale_3_valley.json`
│   ├── `log_prime_scale_6_peak.json`
│   ├── `log_prime_scale_6_valley.json`
│   ├── `manifest.json`
│   ├── `pure_prime_scale_128_primes.json`
│   ├── `sample_scale.json`
│   └── `terrain_scale_8_valley.json`
├── **readmes/**
│   ├── `code_paste_template.md`
│   ├── `final_architecture_README.md`
│   ├── `nextgen_README_consolidated.md`
│   ├── `prime_scale_cheatsheet_fullpath.txt`
│   └── `prime_scale_drive_scripts_README.md`
├── **scripts/**
│   ├── `__init__.py`
│   ├── `binary_gap_analyzer.py`
│   ├── `cluster_finder.py`
│   ├── `core_pure_prime_scale.py`
│   ├── `core_terrain_scale.py`
│   ├── `gap_threshold_scout.py`
│   ├── `main.py`
│   └── `scale_utils.py`
└── `viewer.js`

---

## Project Architecture Snapshot

**/home/mint/prime-scale-html-viewer**

        `index.html`
        ```html
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="UTF-8">
          <title>Prime Scale Viewer</title>
        </head>
        <body>
          <h1>Prime Scale Viewer</h1>
          <div id="scale-display">Loading scale...</div>
          <script src="viewer.js"></script>
        </body>
        </html>
        ```

        **output/**

            `output/gap_scout_match_5_notes.json`
            ```json
            {
              "name": "gap_scout_match_5_notes",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07480798051337051,
                  "frequency": 231.70858596251097,
                  "midi": 58,
                  "cents_from_base": 89.76957661604462,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6107910531958953,
                  "frequency": 335.9611884703146,
                  "midi": 64,
                  "cents_from_base": 732.9492638350744,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6728648404106712,
                  "frequency": 350.73182965589353,
                  "midi": 65,
                  "cents_from_base": 807.4378084928054,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7630023064687417,
                  "frequency": 373.34407362361526,
                  "midi": 66,
                  "cents_from_base": 915.60276776249,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9068881985485664,
                  "frequency": 412.4993146254886,
                  "midi": 68,
                  "cents_from_base": 1088.2658382582797,
                  "prime_sources": []
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/log_prime_scale_13_valley.json`
            ```json
            {
              "name": "log_prime_scale_13_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.029291666666666667,
                  "frequency": 224.5124096554435,
                  "midi": 57,
                  "cents_from_base": 35.15,
                  "prime_sources": [
                    66863,
                    66877,
                    66883,
                    66889
                  ]
                },
                {
                  "log_position": 0.12095833333333333,
                  "frequency": 239.24053635066036,
                  "midi": 58,
                  "cents_from_base": 145.15,
                  "prime_sources": [
                    71249,
                    71257,
                    71261,
                    71263,
                    71287
                  ]
                },
                {
                  "log_position": 0.17775,
                  "frequency": 248.84605635407974,
                  "midi": 59,
                  "cents_from_base": 213.29999999999998,
                  "prime_sources": [
                    37057,
                    37061,
                    74131,
                    74143,
                    74149
                  ]
                },
                {
                  "log_position": 0.25783333333333336,
                  "frequency": 263.0499648117823,
                  "midi": 60,
                  "cents_from_base": 309.40000000000003,
                  "prime_sources": [
                    39181,
                    39191,
                    78341,
                    78347,
                    78367
                  ]
                },
                {
                  "log_position": 0.363375,
                  "frequency": 283.0150009385238,
                  "midi": 61,
                  "cents_from_base": 436.05,
                  "prime_sources": [
                    42157,
                    84299,
                    84307,
                    84313,
                    84317,
                    84319
                  ]
                },
                {
                  "log_position": 0.3879166666666667,
                  "frequency": 287.8705471850103,
                  "midi": 62,
                  "cents_from_base": 465.5,
                  "prime_sources": [
                    21433,
                    42863,
                    85733,
                    85751,
                    85781
                  ]
                },
                {
                  "log_position": 0.5134166666666666,
                  "frequency": 314.03387470162096,
                  "midi": 63,
                  "cents_from_base": 616.0999999999999,
                  "prime_sources": [
                    46769,
                    46771,
                    93523,
                    93529,
                    93553,
                    93557,
                    93559,
                    93563
                  ]
                },
                {
                  "log_position": 0.560375,
                  "frequency": 324.42354431975815,
                  "midi": 64,
                  "cents_from_base": 672.4499999999999,
                  "prime_sources": [
                    24169,
                    48311,
                    48313,
                    48337,
                    96643,
                    96661,
                    96667,
                    96671
                  ]
                },
                {
                  "log_position": 0.6490833333333333,
                  "frequency": 344.9977270679486,
                  "midi": 65,
                  "cents_from_base": 778.9,
                  "prime_sources": [
                    25693,
                    51383,
                    102761,
                    102763,
                    102769,
                    102793,
                    102797
                  ]
                },
                {
                  "log_position": 0.7498333333333334,
                  "frequency": 369.95168174867587,
                  "midi": 66,
                  "cents_from_base": 899.8000000000001,
                  "prime_sources": [
                    27551,
                    55103,
                    55109,
                    55117,
                    110183,
                    110221,
                    110233,
                    110237
                  ]
                },
                {
                  "log_position": 0.7719583333333333,
                  "frequency": 375.66894443090075,
                  "midi": 66,
                  "cents_from_base": 926.3499999999999,
                  "prime_sources": [
                    27983,
                    55949,
                    55967,
                    111871,
                    111893,
                    111913,
                    111919
                  ]
                },
                {
                  "log_position": 0.8587916666666666,
                  "frequency": 398.9741264473833,
                  "midi": 67,
                  "cents_from_base": 1030.55,
                  "prime_sources": [
                    29717,
                    59407,
                    59417,
                    59419,
                    59441,
                    59443,
                    118819,
                    118831,
                    118843,
                    118861,
                    118873,
                    118891
                  ]
                },
                {
                  "log_position": 0.98725,
                  "frequency": 436.12857661178026,
                  "midi": 69,
                  "cents_from_base": 1184.7,
                  "prime_sources": [
                    32479,
                    64937,
                    64951,
                    64969
                  ]
                }
              ]
            }
            ```

            `output/log_prime_scale_3_valley.json`
            ```json
            {
              "name": "log_prime_scale_3_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.1804,
                  "frequency": 249.3035668094442,
                  "midi": 59,
                  "cents_from_base": 216.48000000000002,
                  "prime_sources": [
                    1163,
                    4637,
                    4639,
                    4643,
                    4649,
                    4651,
                    4657,
                    9257,
                    9277,
                    9281,
                    9283,
                    9293,
                    9311,
                    9319
                  ]
                },
                {
                  "log_position": 0.6138,
                  "frequency": 336.6626147773795,
                  "midi": 64,
                  "cents_from_base": 736.5600000000001,
                  "prime_sources": [
                    1567,
                    1571,
                    3137,
                    6247,
                    6257,
                    6263,
                    6269,
                    6271,
                    6277,
                    6287,
                    12487,
                    12491,
                    12497,
                    12503,
                    12511,
                    12517,
                    12527,
                    12539,
                    12541,
                    12547,
                    12553,
                    12569,
                    12577,
                    12583
                  ]
                },
                {
                  "log_position": 0.6698,
                  "frequency": 349.9875309149005,
                  "midi": 65,
                  "cents_from_base": 803.76,
                  "prime_sources": [
                    1627,
                    3251,
                    3253,
                    3257,
                    3259,
                    3271,
                    6491,
                    6521,
                    6529,
                    12979,
                    12983,
                    13001,
                    13003,
                    13007,
                    13009,
                    13033,
                    13037,
                    13043,
                    13049,
                    13063
                  ]
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/log_prime_scale_6_peak.json`
            ```json
            {
              "name": "log_prime_scale_6_peak",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": [
                    2,
                    4091,
                    4093,
                    4099,
                    8179,
                    8191,
                    8209,
                    16361,
                    16363,
                    16369,
                    16381,
                    16411,
                    16417,
                    32707,
                    32713,
                    32717,
                    32719,
                    32749,
                    32771,
                    32779,
                    32783,
                    32789,
                    32797,
                    32801,
                    32803,
                    32831,
                    32833
                  ]
                },
                {
                  "log_position": 0.322,
                  "frequency": 275.013706568746,
                  "midi": 61,
                  "cents_from_base": 386.40000000000003,
                  "prime_sources": [
                    5,
                    641,
                    1279,
                    2557,
                    5113,
                    5119,
                    10223,
                    10243,
                    10247,
                    10253,
                    10259,
                    20441,
                    20443,
                    20477,
                    20479,
                    20483,
                    20507,
                    20509,
                    20521
                  ]
                },
                {
                  "log_position": 0.4594,
                  "frequency": 302.493370370937,
                  "midi": 63,
                  "cents_from_base": 551.28,
                  "prime_sources": [
                    11,
                    1409,
                    2819,
                    5623,
                    5639,
                    5641,
                    11243,
                    11251,
                    11257,
                    11261,
                    11273,
                    11279,
                    11287,
                    22481,
                    22483,
                    22501,
                    22511,
                    22531,
                    22541,
                    22543,
                    22549,
                    22567,
                    22571,
                    22573
                  ]
                },
                {
                  "log_position": 0.585,
                  "frequency": 330.00857764287997,
                  "midi": 64,
                  "cents_from_base": 702.0,
                  "prime_sources": [
                    3,
                    769,
                    3067,
                    6133,
                    6143,
                    6151,
                    12263,
                    12269,
                    12277,
                    12281,
                    12289,
                    12301,
                    24527,
                    24533,
                    24547,
                    24551,
                    24571,
                    24593,
                    24611,
                    24623
                  ]
                },
                {
                  "log_position": 0.8076,
                  "frequency": 385.0654074630357,
                  "midi": 67,
                  "cents_from_base": 969.12,
                  "prime_sources": [
                    7,
                    449,
                    1789,
                    3581,
                    3583,
                    7159,
                    7177,
                    14321,
                    14323,
                    14327,
                    14341,
                    14347,
                    28619,
                    28621,
                    28627,
                    28631,
                    28643,
                    28649,
                    28657,
                    28661,
                    28663,
                    28669,
                    28687,
                    28697,
                    28703,
                    28711,
                    28723,
                    28729
                  ]
                },
                {
                  "log_position": 0.9998,
                  "frequency": 439.9390072759019,
                  "midi": 69,
                  "cents_from_base": 1199.76,
                  "prime_sources": [
                    2,
                    4091,
                    4093,
                    4099,
                    8179,
                    8191,
                    16349,
                    16361,
                    16363,
                    16369,
                    16381,
                    16411,
                    32707,
                    32713,
                    32717,
                    32719,
                    32749,
                    32771,
                    32779,
                    32783,
                    32789,
                    32797,
                    32801,
                    32803,
                    32831
                  ]
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/log_prime_scale_6_valley.json`
            ```json
            {
              "name": "log_prime_scale_6_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.075375,
                  "frequency": 231.79967181348457,
                  "midi": 58,
                  "cents_from_base": 90.45,
                  "prime_sources": [
                    8623,
                    8627,
                    8629,
                    8641,
                    17239,
                    17257,
                    34483,
                    34487,
                    34499,
                    34501,
                    34511,
                    34513,
                    34519,
                    34537,
                    34543,
                    34549
                  ]
                },
                {
                  "log_position": 0.176875,
                  "frequency": 248.6951760388849,
                  "midi": 59,
                  "cents_from_base": 212.25,
                  "prime_sources": [
                    9257,
                    18503,
                    18517,
                    18521,
                    18523,
                    18539,
                    18541,
                    36997,
                    37003,
                    37013,
                    37019,
                    37021,
                    37039,
                    37049,
                    37057,
                    37061,
                    37087
                  ]
                },
                {
                  "log_position": 0.43675,
                  "frequency": 297.78137534016145,
                  "midi": 62,
                  "cents_from_base": 524.1,
                  "prime_sources": [
                    11083,
                    11087,
                    11093,
                    22147,
                    22153,
                    22157,
                    22159,
                    22171,
                    22189,
                    22193,
                    44293,
                    44351,
                    44357,
                    44371,
                    44381,
                    44383,
                    44389
                  ]
                },
                {
                  "log_position": 0.610625,
                  "frequency": 335.9225217964596,
                  "midi": 64,
                  "cents_from_base": 732.75,
                  "prime_sources": [
                    6247,
                    6257,
                    12497,
                    12503,
                    12511,
                    12517,
                    24989,
                    25013,
                    25031,
                    25033,
                    25037,
                    49991,
                    49993,
                    49999,
                    50021,
                    50023,
                    50033,
                    50047,
                    50051,
                    50053,
                    50069,
                    50077,
                    50087,
                    50093,
                    50101
                  ]
                },
                {
                  "log_position": 0.6735,
                  "frequency": 350.88627652385884,
                  "midi": 65,
                  "cents_from_base": 808.1999999999999,
                  "prime_sources": [
                    6529,
                    13049,
                    13063,
                    26099,
                    26107,
                    26111,
                    26113,
                    26119,
                    26141,
                    26153,
                    26161,
                    52201,
                    52223,
                    52237,
                    52249,
                    52253,
                    52259,
                    52267,
                    52289,
                    52291,
                    52301,
                    52313,
                    52321
                  ]
                },
                {
                  "log_position": 0.958625,
                  "frequency": 427.56048438765623,
                  "midi": 69,
                  "cents_from_base": 1150.35,
                  "prime_sources": [
                    7951,
                    7963,
                    15901,
                    15907,
                    15913,
                    15919,
                    15923,
                    15937,
                    31799,
                    31817,
                    31847,
                    31849,
                    31859,
                    31873,
                    31883
                  ]
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/manifest.json`
            ```json
            {
              "scales": [
                "gap_scout_match_5_notes.json",
                "log_prime_scale_3_valley.json",
                "log_prime_scale_6_valley.json",
                "log_prime_scale_6_peak.json",
                "log_prime_scale_13_valley.json",
                "pure_prime_scale_128_primes.json",
                "sample_scale.json",
                "terrain_scale_8_valley.json"
              ]
            }
            ```

            `output/pure_prime_scale_128_primes.json`
            ```json
            {
              "name": "pure_prime_scale_128_primes",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5849625007211562,
                  "frequency": 330.0,
                  "midi": 64,
                  "cents_from_base": 701.9550008653874,
                  "prime_sources": []
                },
                {
                  "log_position": 0.32192809488736235,
                  "frequency": 275.0,
                  "midi": 61,
                  "cents_from_base": 386.3137138648348,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8073549220576041,
                  "frequency": 385.0,
                  "midi": 67,
                  "cents_from_base": 968.8259064691249,
                  "prime_sources": []
                },
                {
                  "log_position": 0.45943161863729726,
                  "frequency": 302.5,
                  "midi": 63,
                  "cents_from_base": 551.3179423647567,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7004397181410922,
                  "frequency": 357.5,
                  "midi": 65,
                  "cents_from_base": 840.5276617693106,
                  "prime_sources": []
                },
                {
                  "log_position": 0.0874628412503394,
                  "frequency": 233.75,
                  "midi": 58,
                  "cents_from_base": 104.95540950040728,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2479275134435855,
                  "frequency": 261.25,
                  "midi": 60,
                  "cents_from_base": 297.5130161323026,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5235619560570128,
                  "frequency": 316.25,
                  "midi": 63,
                  "cents_from_base": 628.2743472684155,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8579809951275721,
                  "frequency": 398.75,
                  "midi": 67,
                  "cents_from_base": 1029.5771941530866,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9541963103868752,
                  "frequency": 426.25,
                  "midi": 68,
                  "cents_from_base": 1145.0355724642502,
                  "prime_sources": []
                },
                {
                  "log_position": 0.20945336562894978,
                  "frequency": 254.375,
                  "midi": 60,
                  "cents_from_base": 251.34403875473973,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3575520046180837,
                  "frequency": 281.875,
                  "midi": 61,
                  "cents_from_base": 429.0624055417004,
                  "prime_sources": []
                },
                {
                  "log_position": 0.42626475470209796,
                  "frequency": 295.625,
                  "midi": 62,
                  "cents_from_base": 511.51770564251757,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5545888516776374,
                  "frequency": 323.125,
                  "midi": 64,
                  "cents_from_base": 665.5066220131648,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7279204545631992,
                  "frequency": 364.375,
                  "midi": 66,
                  "cents_from_base": 873.504545475839,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8826430493618412,
                  "frequency": 405.625,
                  "midi": 68,
                  "cents_from_base": 1059.1716592342095,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9307373375628862,
                  "frequency": 419.375,
                  "midi": 68,
                  "cents_from_base": 1116.8848050754634,
                  "prime_sources": []
                },
                {
                  "log_position": 0.06608919045777244,
                  "frequency": 230.3125,
                  "midi": 58,
                  "cents_from_base": 79.30702854932693,
                  "prime_sources": []
                },
                {
                  "log_position": 0.14974711950468206,
                  "frequency": 244.0625,
                  "midi": 59,
                  "cents_from_base": 179.69654340561846,
                  "prime_sources": []
                },
                {
                  "log_position": 0.18982455888001723,
                  "frequency": 250.9375,
                  "midi": 59,
                  "cents_from_base": 227.78947065602068,
                  "prime_sources": []
                },
                {
                  "log_position": 0.30378074817710293,
                  "frequency": 271.5625,
                  "midi": 61,
                  "cents_from_base": 364.53689781252353,
                  "prime_sources": []
                },
                {
                  "log_position": 0.37503943134692475,
                  "frequency": 285.3125,
                  "midi": 62,
                  "cents_from_base": 450.04731761630967,
                  "prime_sources": []
                },
                {
                  "log_position": 0.47573343096639775,
                  "frequency": 305.9375,
                  "midi": 63,
                  "cents_from_base": 570.8801171596773,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5999128421871277,
                  "frequency": 333.4375,
                  "midi": 64,
                  "cents_from_base": 719.8954106245533,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6582114827517948,
                  "frequency": 347.1875,
                  "midi": 65,
                  "cents_from_base": 789.8537793021537,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6865005271832184,
                  "frequency": 354.0625,
                  "midi": 65,
                  "cents_from_base": 823.8006326198621,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7414669864011469,
                  "frequency": 367.8125,
                  "midi": 66,
                  "cents_from_base": 889.7603836813763,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7681843247769263,
                  "frequency": 374.6875,
                  "midi": 66,
                  "cents_from_base": 921.8211897323116,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8201789624151877,
                  "frequency": 388.4375,
                  "midi": 67,
                  "cents_from_base": 984.2147548982252,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9886846867721658,
                  "frequency": 436.5625,
                  "midi": 69,
                  "cents_from_base": 1186.421624126599,
                  "prime_sources": []
                },
                {
                  "log_position": 0.03342300153745028,
                  "frequency": 225.15625,
                  "midi": 57,
                  "cents_from_base": 40.10760184494033,
                  "prime_sources": []
                },
                {
                  "log_position": 0.09803208296052672,
                  "frequency": 235.46875,
                  "midi": 58,
                  "cents_from_base": 117.63849955263207,
                  "prime_sources": []
                },
                {
                  "log_position": 0.11894107272350743,
                  "frequency": 238.90625,
                  "midi": 58,
                  "cents_from_base": 142.7292872682089,
                  "prime_sources": []
                },
                {
                  "log_position": 0.21916852046216156,
                  "frequency": 256.09375,
                  "midi": 60,
                  "cents_from_base": 263.00222455459385,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2384047393250789,
                  "frequency": 259.53125,
                  "midi": 60,
                  "cents_from_base": 286.0856871900947,
                  "prime_sources": []
                },
                {
                  "log_position": 0.294620748891627,
                  "frequency": 269.84375,
                  "midi": 61,
                  "cents_from_base": 353.5448986699524,
                  "prime_sources": []
                },
                {
                  "log_position": 0.34872815423107756,
                  "frequency": 280.15625,
                  "midi": 61,
                  "cents_from_base": 418.4737850772931,
                  "prime_sources": []
                },
                {
                  "log_position": 0.38370429247405224,
                  "frequency": 287.03125,
                  "midi": 62,
                  "cents_from_base": 460.4451509688627,
                  "prime_sources": []
                },
                {
                  "log_position": 0.43462822763672465,
                  "frequency": 297.34375,
                  "midi": 62,
                  "cents_from_base": 521.5538731640696,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4838157772642564,
                  "frequency": 307.65625,
                  "midi": 63,
                  "cents_from_base": 580.5789327171077,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4998458870832054,
                  "frequency": 311.09375,
                  "midi": 63,
                  "cents_from_base": 599.8150644998465,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5774288280357487,
                  "frequency": 328.28125,
                  "midi": 64,
                  "cents_from_base": 692.9145936428985,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5924570372680804,
                  "frequency": 331.71875,
                  "midi": 64,
                  "cents_from_base": 710.9484447216965,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6220518194563762,
                  "frequency": 338.59375,
                  "midi": 64,
                  "cents_from_base": 746.4621833476515,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6366246205436489,
                  "frequency": 342.03125,
                  "midi": 65,
                  "cents_from_base": 763.9495446523787,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7210991887071851,
                  "frequency": 362.65625,
                  "midi": 66,
                  "cents_from_base": 865.3190264486221,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8008998999203047,
                  "frequency": 383.28125,
                  "midi": 67,
                  "cents_from_base": 961.0798799043657,
                  "prime_sources": []
                },
                {
                  "log_position": 0.826548487290915,
                  "frequency": 390.15625,
                  "midi": 67,
                  "cents_from_base": 991.858184749098,
                  "prime_sources": []
                },
                {
                  "log_position": 0.839203788096944,
                  "frequency": 393.59375,
                  "midi": 67,
                  "cents_from_base": 1007.0445457163328,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8641861446542802,
                  "frequency": 400.46875,
                  "midi": 67,
                  "cents_from_base": 1037.0233735851364,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9008668079807486,
                  "frequency": 410.78125,
                  "midi": 68,
                  "cents_from_base": 1081.0401695768983,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9128893362299616,
                  "frequency": 414.21875,
                  "midi": 68,
                  "cents_from_base": 1095.467203475954,
                  "prime_sources": []
                },
                {
                  "log_position": 0.971543553950772,
                  "frequency": 431.40625,
                  "midi": 69,
                  "cents_from_base": 1165.8522647409263,
                  "prime_sources": []
                },
                {
                  "log_position": 0.005624549193878107,
                  "frequency": 220.859375,
                  "midi": 57,
                  "cents_from_base": 6.749459032653728,
                  "prime_sources": []
                },
                {
                  "log_position": 0.03891898929230235,
                  "frequency": 226.015625,
                  "midi": 57,
                  "cents_from_base": 46.70278715076282,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07146236255662415,
                  "frequency": 231.171875,
                  "midi": 58,
                  "cents_from_base": 85.75483506794897,
                  "prime_sources": []
                },
                {
                  "log_position": 0.08214904135387156,
                  "frequency": 232.890625,
                  "midi": 58,
                  "cents_from_base": 98.57884962464587,
                  "prime_sources": []
                },
                {
                  "log_position": 0.11374216604918833,
                  "frequency": 238.046875,
                  "midi": 58,
                  "cents_from_base": 136.490599259026,
                  "prime_sources": []
                },
                {
                  "log_position": 0.1344263202209261,
                  "frequency": 241.484375,
                  "midi": 59,
                  "cents_from_base": 161.31158426511132,
                  "prime_sources": []
                },
                {
                  "log_position": 0.14465824283188233,
                  "frequency": 243.203125,
                  "midi": 59,
                  "cents_from_base": 173.5898913982588,
                  "prime_sources": []
                },
                {
                  "log_position": 0.19475685442224788,
                  "frequency": 251.796875,
                  "midi": 59,
                  "cents_from_base": 233.70822530669747,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2620948453701794,
                  "frequency": 263.828125,
                  "midi": 60,
                  "cents_from_base": 314.5138144442153,
                  "prime_sources": []
                },
                {
                  "log_position": 0.28077077013060253,
                  "frequency": 267.265625,
                  "midi": 60,
                  "cents_from_base": 336.924924156723,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2900188469326183,
                  "frequency": 268.984375,
                  "midi": 60,
                  "cents_from_base": 348.022616319142,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3083390301394073,
                  "frequency": 272.421875,
                  "midi": 61,
                  "cents_from_base": 370.0068361672887,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3706874068072177,
                  "frequency": 284.453125,
                  "midi": 61,
                  "cents_from_base": 444.82488816866123,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3966047811818585,
                  "frequency": 289.609375,
                  "midi": 62,
                  "cents_from_base": 475.9257374182302,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4387918525782609,
                  "frequency": 298.203125,
                  "midi": 62,
                  "cents_from_base": 526.5502230939131,
                  "prime_sources": []
                },
                {
                  "log_position": 0.44708322620965224,
                  "frequency": 299.921875,
                  "midi": 62,
                  "cents_from_base": 536.4998714515826,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4635243732711803,
                  "frequency": 303.359375,
                  "midi": 63,
                  "cents_from_base": 556.2292479254163,
                  "prime_sources": []
                },
                {
                  "log_position": 0.48784003382305136,
                  "frequency": 308.515625,
                  "midi": 63,
                  "cents_from_base": 585.4080405876616,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5196362528432128,
                  "frequency": 315.390625,
                  "midi": 63,
                  "cents_from_base": 623.5635034118553,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5430318202552378,
                  "frequency": 320.546875,
                  "midi": 64,
                  "cents_from_base": 651.6381843062853,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5660540381710917,
                  "frequency": 325.703125,
                  "midi": 64,
                  "cents_from_base": 679.26484580531,
                  "prime_sources": []
                },
                {
                  "log_position": 0.581200581924957,
                  "frequency": 329.140625,
                  "midi": 64,
                  "cents_from_base": 697.4406983099484,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6036263449861919,
                  "frequency": 334.296875,
                  "midi": 64,
                  "cents_from_base": 724.3516139834303,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6329951971429578,
                  "frequency": 341.171875,
                  "midi": 65,
                  "cents_from_base": 759.5942365715493,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6474584264549202,
                  "frequency": 344.609375,
                  "midi": 65,
                  "cents_from_base": 776.9501117459043,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6759570329417488,
                  "frequency": 351.484375,
                  "midi": 65,
                  "cents_from_base": 811.1484395300986,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7108064336993516,
                  "frequency": 360.078125,
                  "midi": 66,
                  "cents_from_base": 852.9677204392219,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7176764230663961,
                  "frequency": 361.796875,
                  "midi": 66,
                  "cents_from_base": 861.2117076796753,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7515440590890982,
                  "frequency": 370.390625,
                  "midi": 66,
                  "cents_from_base": 901.8528709069178,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7582232147267249,
                  "frequency": 372.109375,
                  "midi": 66,
                  "cents_from_base": 909.8678576720699,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7780771295353582,
                  "frequency": 377.265625,
                  "midi": 66,
                  "cents_from_base": 933.6925554424299,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7911628885550183,
                  "frequency": 380.703125,
                  "midi": 66,
                  "cents_from_base": 949.3954662660219,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8105716347411469,
                  "frequency": 385.859375,
                  "midi": 67,
                  "cents_from_base": 972.6859616893763,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8360503550580697,
                  "frequency": 392.734375,
                  "midi": 67,
                  "cents_from_base": 1003.2604260696836,
                  "prime_sources": []
                },
                {
                  "log_position": 0.848622940429338,
                  "frequency": 396.171875,
                  "midi": 67,
                  "cents_from_base": 1018.3475285152056,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8548683832602364,
                  "frequency": 397.890625,
                  "midi": 67,
                  "cents_from_base": 1025.8420599122837,
                  "prime_sources": []
                },
                {
                  "log_position": 0.867278739709662,
                  "frequency": 401.328125,
                  "midi": 67,
                  "cents_from_base": 1040.7344876515945,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9038818457361802,
                  "frequency": 411.640625,
                  "midi": 68,
                  "cents_from_base": 1084.6582148834163,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9277779620823422,
                  "frequency": 418.515625,
                  "midi": 68,
                  "cents_from_base": 1113.3335544988106,
                  "prime_sources": []
                },
                {
                  "log_position": 0.939579214314693,
                  "frequency": 421.953125,
                  "midi": 68,
                  "cents_from_base": 1127.4950571776317,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9628960053372605,
                  "frequency": 428.828125,
                  "midi": 69,
                  "cents_from_base": 1155.4752064047127,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9744145898055271,
                  "frequency": 432.265625,
                  "midi": 69,
                  "cents_from_base": 1169.2975077666324,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9915218460756953,
                  "frequency": 437.421875,
                  "midi": 69,
                  "cents_from_base": 1189.8262152908344,
                  "prime_sources": []
                },
                {
                  "log_position": 0.025139562278508228,
                  "frequency": 223.8671875,
                  "midi": 57,
                  "cents_from_base": 30.167474734209872,
                  "prime_sources": []
                },
                {
                  "log_position": 0.030667136246941375,
                  "frequency": 224.7265625,
                  "midi": 57,
                  "cents_from_base": 36.80056349632965,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07948478382681526,
                  "frequency": 232.4609375,
                  "midi": 58,
                  "cents_from_base": 95.3817405921783,
                  "prime_sources": []
                },
                {
                  "log_position": 0.09539702279255656,
                  "frequency": 235.0390625,
                  "midi": 58,
                  "cents_from_base": 114.47642735106787,
                  "prime_sources": []
                },
                {
                  "log_position": 0.12153351734003176,
                  "frequency": 239.3359375,
                  "midi": 58,
                  "cents_from_base": 145.8402208080381,
                  "prime_sources": []
                },
                {
                  "log_position": 0.13699111208022957,
                  "frequency": 241.9140625,
                  "midi": 59,
                  "cents_from_base": 164.3893344962755,
                  "prime_sources": []
                },
                {
                  "log_position": 0.15228484230658193,
                  "frequency": 244.4921875,
                  "midi": 59,
                  "cents_from_base": 182.74181076789833,
                  "prime_sources": []
                },
                {
                  "log_position": 0.15734693536284278,
                  "frequency": 245.3515625,
                  "midi": 59,
                  "cents_from_base": 188.81632243541134,
                  "prime_sources": []
                },
                {
                  "log_position": 0.17242750864548248,
                  "frequency": 247.9296875,
                  "midi": 59,
                  "cents_from_base": 206.913010374579,
                  "prime_sources": []
                },
                {
                  "log_position": 0.1972166931100522,
                  "frequency": 252.2265625,
                  "midi": 59,
                  "cents_from_base": 236.66003173206263,
                  "prime_sources": []
                },
                {
                  "log_position": 0.21188829454600366,
                  "frequency": 254.8046875,
                  "midi": 60,
                  "cents_from_base": 254.2659534552044,
                  "prime_sources": []
                },
                {
                  "log_position": 0.22641219278878566,
                  "frequency": 257.3828125,
                  "midi": 60,
                  "cents_from_base": 271.6946313465428,
                  "prime_sources": []
                },
                {
                  "log_position": 0.23122118071118544,
                  "frequency": 258.2421875,
                  "midi": 60,
                  "cents_from_base": 277.46541685342254,
                  "prime_sources": []
                },
                {
                  "log_position": 0.24555270625568207,
                  "frequency": 260.8203125,
                  "midi": 60,
                  "cents_from_base": 294.6632475068185,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2597432636907815,
                  "frequency": 263.3984375,
                  "midi": 60,
                  "cents_from_base": 311.6919164289378,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2691266791494179,
                  "frequency": 265.1171875,
                  "midi": 60,
                  "cents_from_base": 322.9520149793015,
                  "prime_sources": []
                },
                {
                  "log_position": 0.27379559921426466,
                  "frequency": 265.9765625,
                  "midi": 60,
                  "cents_from_base": 328.5547190571176,
                  "prime_sources": []
                },
                {
                  "log_position": 0.301496194982549,
                  "frequency": 271.1328125,
                  "midi": 61,
                  "cents_from_base": 361.79543397905877,
                  "prime_sources": []
                },
                {
                  "log_position": 0.324180546618741,
                  "frequency": 275.4296875,
                  "midi": 61,
                  "cents_from_base": 389.0166559424892,
                  "prime_sources": []
                },
                {
                  "log_position": 0.32867492732794734,
                  "frequency": 276.2890625,
                  "midi": 61,
                  "cents_from_base": 394.4099127935368,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3376219019925075,
                  "frequency": 278.0078125,
                  "midi": 61,
                  "cents_from_base": 405.14628239100904,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3509391815464308,
                  "frequency": 280.5859375,
                  "midi": 61,
                  "cents_from_base": 421.12701785571693,
                  "prime_sources": []
                },
                {
                  "log_position": 0.36413465500805176,
                  "frequency": 283.1640625,
                  "midi": 61,
                  "cents_from_base": 436.9615860096621,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3685064615076917,
                  "frequency": 284.0234375,
                  "midi": 61,
                  "cents_from_base": 442.20775380923,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3944626946103171,
                  "frequency": 289.1796875,
                  "midi": 62,
                  "cents_from_base": 473.3552335323805,
                  "prime_sources": []
                },
                {
                  "log_position": 0.40301202357499677,
                  "frequency": 290.8984375,
                  "midi": 62,
                  "cents_from_base": 483.6144282899961,
                  "prime_sources": []
                },
                {
                  "log_position": 0.41574176829009046,
                  "frequency": 293.4765625,
                  "midi": 62,
                  "cents_from_base": 498.8901219481086,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4325419003882585,
                  "frequency": 296.9140625,
                  "midi": 62,
                  "cents_from_base": 519.0502804659102,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4532706340106232,
                  "frequency": 301.2109375,
                  "midi": 62,
                  "cents_from_base": 543.9247608127478,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4696418172395161,
                  "frequency": 304.6484375,
                  "midi": 63,
                  "cents_from_base": 563.5701806874193,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4898479604392978,
                  "frequency": 308.9453125,
                  "midi": 63,
                  "cents_from_base": 587.8175525271573,
                  "prime_sources": []
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/sample_scale.json`
            ```json
            {
              "name": "sample_scale",
              "base_frequency": 220.0,
              "notes": [
                {
                  "frequency": 220.0,
                  "cents_from_base": 0.0,
                  "midi": 57,
                  "log_position": 0.0,
                  "prime_sources": []
                },
                {
                  "frequency": 246.94,
                  "cents_from_base": 200.0,
                  "midi": 59,
                  "log_position": 0.1667,
                  "prime_sources": [
                    3
                  ]
                },
                {
                  "frequency": 261.63,
                  "cents_from_base": 300.0,
                  "midi": 60,
                  "log_position": 0.25,
                  "prime_sources": [
                    5
                  ]
                },
                {
                  "frequency": 293.66,
                  "cents_from_base": 500.0,
                  "midi": 62,
                  "log_position": 0.4167,
                  "prime_sources": [
                    7
                  ]
                },
                {
                  "frequency": 329.63,
                  "cents_from_base": 700.0,
                  "midi": 64,
                  "log_position": 0.5833,
                  "prime_sources": [
                    11
                  ]
                },
                {
                  "frequency": 392.0,
                  "cents_from_base": 900.0,
                  "midi": 67,
                  "log_position": 0.75,
                  "prime_sources": [
                    13
                  ]
                },
                {
                  "frequency": 440.0,
                  "cents_from_base": 1200.0,
                  "midi": 69,
                  "log_position": 1.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/terrain_scale_8_valley.json`
            ```json
            {
              "name": "terrain_scale_8_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07575,
                  "frequency": 231.85993137814998,
                  "midi": 58,
                  "cents_from_base": 90.89999999999999,
                  "prime_sources": []
                },
                {
                  "log_position": 0.178,
                  "frequency": 248.88918182609805,
                  "midi": 59,
                  "cents_from_base": 213.6,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2845,
                  "frequency": 267.9573749645833,
                  "midi": 60,
                  "cents_from_base": 341.4,
                  "prime_sources": []
                },
                {
                  "log_position": 0.495,
                  "frequency": 310.0505661312443,
                  "midi": 63,
                  "cents_from_base": 594.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.61025,
                  "frequency": 335.8352167377353,
                  "midi": 64,
                  "cents_from_base": 732.3,
                  "prime_sources": []
                },
                {
                  "log_position": 0.672,
                  "frequency": 350.5216423656564,
                  "midi": 65,
                  "cents_from_base": 806.4000000000001,
                  "prime_sources": []
                },
                {
                  "log_position": 0.763,
                  "frequency": 373.3434767505944,
                  "midi": 66,
                  "cents_from_base": 915.6,
                  "prime_sources": []
                },
                {
                  "log_position": 0.95775,
                  "frequency": 427.3012459589087,
                  "midi": 68,
                  "cents_from_base": 1149.3,
                  "prime_sources": []
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

        **readmes/**

            `readmes/code_paste_template.md`
            ```md
            # Prime Scale App – Code Template (Clean Paste Structure)
            
            This markdown provides clean headings and fenced code blocks for you to manually paste in each script's full content.
            
            ---
            
            ## scale_utils.py
            
            ```python
            # Paste full contents of scale_utils.py here
            import math
            import json
            import os
            
            def generate_primes(n):
                primes = [2]
                candidate = 3
                while len(primes) < n:
                    is_prime = True
                    for p in primes:
                        if candidate % p == 0:
                            is_prime = False
                            break
                        if p * p > candidate:
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 2
                return primes
            
            def reduce_value(val):
                while val >= 2:
                    val /= 2
                while val < 1:
                    val *= 2
                return val
            
            def get_log_positions(primes):
                """Return log2 positions of primes reduced to the 1–2 octave range."""
                return [math.log2(reduce_value(p)) for p in primes]
            
            def generate_density_axis(resolution):
                """Returns evenly spaced samples from 0 to 1 (not inclusive) for log-space rendering."""
                return [i / resolution for i in range(resolution)]
            
            def circular_distance(a, b):
                return min(abs(a - b), 1 - abs(a - b))
            
            def prime_weight(p, curve=1.0):
                if curve == 0.0:
                    return 1.0
                return 1 / (p ** curve)
            
            def add_bounds(notes, base_freq):
                bounds = [
                    {
                        "log_position": 0.0,
                        "frequency": base_freq,
                        "midi": round(69 + 12 * math.log2(base_freq / 440.0)),
                        "cents_from_base": 0.0,
                        "prime_sources": []
                    },
                    {
                        "log_position": 1.0,
                        "frequency": base_freq * 2,
                        "midi": round(69 + 12 * math.log2((base_freq * 2) / 440.0)),
                        "cents_from_base": 1200.0,
                        "prime_sources": []
                    }
                ]
                return [bounds[0]] + notes + [bounds[1]]
            
            def export_json(scale_data, filename):
                # Always write to top-level /output/ folder
                script_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.dirname(script_dir)
                output_dir = os.path.join(project_root, "output")
            
                os.makedirs(output_dir, exist_ok=True)
                full_path = os.path.join(output_dir, os.path.basename(filename))
            
                with open(full_path, "w", encoding="utf-8") as f:
                    json.dump(scale_data, f, indent=2)
            
                print(f"✔ Saved scale to {full_path}")
            ```
            
            ---
            
            ## core_terrain_scale.py
            
            ```python
            # Paste full contents of core_terrain_scale.py here
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                prime_weight,
                circular_distance,
                generate_density_axis,
                add_bounds,
                export_json
            )
            
            # Terrain-specific smoothing function
            def gravitational_fade(d, w, n=2.5):
                relative = d / (w / 2)
                return 1 / (1 + (relative ** n))
            
            # Generate density map across log2-reduced space
            def generate_density_map(log_positions, weights, resolution, window_size):
                x_axis = generate_density_axis(resolution)
                density_map = []
            
                for x in x_axis:
                    total_weight = 0
                    for log_pos, weight in zip(log_positions, weights):
                        distance = circular_distance(log_pos, x)
                        if distance <= window_size / 2:
                            focus = gravitational_fade(distance, window_size)
                            total_weight += weight * focus
                    density_map.append(total_weight)
            
                return x_axis, density_map
            
            # Segment and select notes from density map
            def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                segment_width = 1.0 / num_notes
                selected_notes = []
            
                for i in range(num_notes):
                    segment_start = i * segment_width
                    segment_end = segment_start + segment_width
                    segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
            
                    if segment_range:
                        best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                        freq = base_frequency * (2 ** best_x)
                        selected_notes.append({
                            "log_position": best_x,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * best_x,
                            "prime_sources": []
                        })
            
                return selected_notes
            
            # Full generator function
            def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                weights = [prime_weight(p, weight_curve) for p in primes]
            
                x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
            
                if include_bounds:
                    selected_notes = add_bounds(selected_notes, base_frequency)
            
                scale_data = {
                    "name": f"terrain_scale_{num_notes}_{mode}",
                    "base_frequency": base_frequency,
                    "notes": selected_notes
                }
            
                filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                export_json(scale_data, filename)
            
            # CLI runner
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, default=1000)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--num-notes", type=int, default=8)
                parser.add_argument("--window-size", type=float, default=0.007)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.add_argument("--weight-curve", type=float, default=1.0)
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_terrain_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode,
                    include_bounds=args.include_bounds,
                    weight_curve=args.weight_curve
                )
            ```
            
            ---
            
            ## gap_threshold_scout.py
            
            ```python
            # Paste full contents of gap_threshold_scout.py here
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility or plotting if needed
            )
            
            # Count qualifying gaps for a given threshold
            def detect_gap_count(log_positions, threshold):
                log_positions.sort()
                gap_centers = []
            
                for i in range(len(log_positions) - 1):
                    gap = log_positions[i + 1] - log_positions[i]
                    if gap >= threshold:
                        center_log = (log_positions[i] + log_positions[i + 1]) / 2
                        gap_centers.append(center_log)
            
                return gap_centers
            
            # Scan thresholds to find ones that match note goal
            def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                matches = []
            
                # Optional: could use this for visual overlays or precision matching later
                _ = generate_density_axis(density_resolution)
            
                current = threshold_min
                while current <= threshold_max:
                    gap_centers = detect_gap_count(log_positions, current)
                    count = len(gap_centers)
            
                    if abs(count - note_goal) <= tolerance:
                        print(f"✔ Match: {count} notes at threshold {current:.6f}")
                        matches.append((current, count, gap_centers))
                    else:
                        print(f"... Skipped: {count} notes at threshold {current:.6f}")
            
                    current = round(current + step_size, 10)  # Avoid float rounding errors
            
                if matches:
                    best_thresh, best_count, best_centers = matches[0]
                    notes = []
                    for log_pos in best_centers:
                        freq = base_frequency * (2 ** log_pos)
                        notes.append({
                            "log_position": log_pos,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * log_pos,
                            "prime_sources": []
                        })
            
                    if include_bounds:
                        notes = add_bounds(notes, base_frequency)
            
                    scale_data = {
                        "name": f"gap_scout_match_{best_count}_notes",
                        "base_frequency": base_frequency,
                        "notes": notes
                    }
            
                    export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
                else:
                    print("No matching thresholds found within specified range.")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                parser.add_argument("--step-size", type=float, default=0.001)
                parser.add_argument("--note-goal", type=int, required=True)
                parser.add_argument("--tolerance", type=int, default=1)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                scan_thresholds(
                    prime_count=args.prime_count,
                    threshold_min=args.threshold_range[0],
                    threshold_max=args.threshold_range[1],
                    step_size=args.step_size,
                    note_goal=args.note_goal,
                    tolerance=args.tolerance,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            
            ```
            
            ---
            
            ## core_pure_prime_scale.py
            
            ```python
            # Paste full contents of core_pure_prime_scale.py here
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility and visualization
            )
            
            def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
            
                # Optional: generate axis for any future visualization
                _ = generate_density_axis(density_resolution)
            
                notes = []
                for log_pos in log_positions:
                    freq = base_frequency * (2 ** log_pos)
                    notes.append({
                        "log_position": log_pos,
                        "frequency": freq,
                        "midi": round(69 + 12 * math.log2(freq / 440.0)),
                        "cents_from_base": 1200 * log_pos,
                        "prime_sources": []
                    })
            
                if include_bounds:
                    notes = add_bounds(notes, base_frequency)
            
                scale_data = {
                    "name": f"pure_prime_scale_{prime_count}_primes",
                    "base_frequency": base_frequency,
                    "notes": notes
                }
            
                export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_pure_prime_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            
            ```
            
            ---
            
            ## binary_gap_analyzer.py
            
            ```python
            # Paste full contents of binary_gap_analyzer.py here
            
            import math
            
            def reduce_value(x):
                while x >= 2:
                    x /= 2
                return x
            
            def generate_primes(n):
                primes = []
                candidate = 2
                while candidate <= n:
                    is_prime = True
                    for p in primes:
                        if p * p > candidate:
                            break
                        if candidate % p == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 1
                return primes
            
            def compute_reduced_primes(tier):
                primes = generate_primes(tier)
                reduced = [reduce_value(p) for p in primes]
                return sorted(reduced), primes
            
            def compute_segment_gaps(reduced, tier):
                segment_width = 1 / (tier // 2)
                segments = []
                for i in range(len(reduced) - 1):
                    start = reduced[i]
                    end = reduced[i + 1]
                    gap = end - start
                    segment_count = round(gap / segment_width)
                    segments.append((start, end, segment_count))
                return segments, segment_width
            
            ```
            
            ---
            
            ## cluster_finder.py
            
            ```python
            # Paste full contents of cluster_finder.py here
            
            import argparse
            from binary_gap_analyzer import compute_reduced_primes, compute_segment_gaps
            import math
            
            def log_center(start, end):
                return math.sqrt(start * end)
            
            def find_clusters(segments, threshold=4):
                clusters = []
                current_cluster = []
                for start, end, count in segments:
                    if count >= threshold:
                        if current_cluster:
                            clusters.append(current_cluster)
                            current_cluster = []
                    else:
                        current_cluster.append((start, end))
                if current_cluster:
                    clusters.append(current_cluster)
                return clusters
            
            def main():
                parser = argparse.ArgumentParser(description="Cluster Finder based on segment gaps.")
                parser.add_argument("--tier", type=int, required=True, help="Binary segmentation tier (must be power of two)")
                args = parser.parse_args()
            
                reduced, _ = compute_reduced_primes(args.tier)
                segment_data, segment_width = compute_segment_gaps(reduced, args.tier)
            
                clusters = find_clusters(segment_data)
            
                print(f"Tier: {args.tier} | Segment Width: {segment_width:.6f}")
                print(f"Found {len(clusters)} cluster(s):\n")
            
                for idx, cluster in enumerate(clusters):
                    cluster_start = cluster[0][0]
                    cluster_end = cluster[-1][1]
                    center = log_center(cluster_start, cluster_end)
                    print(f"Cluster {idx + 1}:")
                    print(f"  Range: {cluster_start:.6f} -> {cluster_end:.6f}")
                    print(f"  Log Center: {center:.6f}")
                    print(f"  Members: {len(cluster)} segments\n")
            
            if __name__ == "__main__":
                main()
            
            ```
            
            ---
            
            ## main.py (planned CLI entry point)
            
            ```python
            # Paste full contents of main.py when implemented
            """
            Prime Scale App – CLI Entry Point
            
            Usage (run from project root):
              python -m scripts.main --scale-type terrain ...
              python -m scripts.main --scale-type gap ...
              python -m scripts.main --scale-type pure ...
            """
            
            import argparse
            from scripts.core_terrain_scale import generate_terrain_scale
            from scripts.gap_threshold_scout import scan_thresholds
            from scripts.core_pure_prime_scale import generate_pure_prime_scale
            
            def main():
                parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
                subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
            
                # Terrain scale CLI
                terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
                terrain_parser.add_argument("--prime-count", type=int, default=1000)
                terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
                terrain_parser.add_argument("--num-notes", type=int, default=8)
                terrain_parser.add_argument("--window-size", type=float, default=0.007)
                terrain_parser.add_argument("--density-resolution", type=int, default=4000)
                terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
                terrain_parser.set_defaults(include_bounds=True)
            
                # Gap scale CLI
                gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
                gap_parser.add_argument("--prime-count", type=int, required=True)
                gap_parser.add_argument("--base-frequency", type=float, default=220.0)
                gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                gap_parser.add_argument("--step-size", type=float, default=0.001)
                gap_parser.add_argument("--note-goal", type=int, required=True)
                gap_parser.add_argument("--tolerance", type=int, default=1)
                gap_parser.add_argument("--density-resolution", type=int, default=4000)
                gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                gap_parser.set_defaults(include_bounds=True)
            
                # Pure scale CLI
                pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
                pure_parser.add_argument("--prime-count", type=int, required=True)
                pure_parser.add_argument("--base-frequency", type=float, default=220.0)
                pure_parser.add_argument("--density-resolution", type=int, default=4000)
                pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                pure_parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                if args.scale_type == "terrain":
                    generate_terrain_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        num_notes=args.num_notes,
                        window_size=args.window_size,
                        density_resolution=args.density_resolution,
                        mode=args.mode,
                        include_bounds=args.include_bounds,
                        weight_curve=args.weight_curve
                    )
            
                elif args.scale_type == "gap":
                    scan_thresholds(
                        prime_count=args.prime_count,
                        threshold_min=args.threshold_range[0],
                        threshold_max=args.threshold_range[1],
                        step_size=args.step_size,
                        note_goal=args.note_goal,
                        tolerance=args.tolerance,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
                elif args.scale_type == "pure":
                    generate_pure_prime_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
            if __name__ == "__main__":
                main()
            ```
            ```

            `readmes/final_architecture_README.md`
            ```md
            # Prime Scale App: Final Architecture & Packaging Strategy
            
            _Last updated: 2025-05-06_
            
            This README consolidates and replaces previous frontend and architecture planning documents. It defines the final architecture and development direction for the Prime Scale App as a modular, JavaScript-based APK-ready environment.
            
            ---
            
            ## Core Principles
            
            - **Frontend-first, JavaScript-native**
            - **APK and PWA compatible** (Capacitor.js recommended)
            - **Modular algorithm support** via drop-in JavaScript packages
            - **No Python dependency required** for scale generation
            - **Developer- and user-friendly** with hot-loadable modules and clean packaging
            
            ---
            
            ## Directory Structure
            
            ```
            /prime-scale-app/
            ├── /public/               # Static assets (icon, manifest, splash)
            ├── /src/
            │   ├── /modules/          # Scale algorithm modules (JS)
            │   ├── /components/       # React components (tool popups, viewers, tray)
            │   ├── /utils/            # Shared JS utilities (e.g. note conversion)
            │   ├── /data/             # modules.json manifest + preloaded scales
            │   └── App.jsx            # Main React app shell
            ├── /output/               # User-generated JSON scales (persistent)
            ├── /android/              # APK wrapper config (via Capacitor)
            ├── /README.md             # (This file)
            └── vite.config.js         # Vite bundler setup
            ```
            
            ---
            
            ## Modular Loader System
            
            Each module is a self-contained JavaScript file exporting a single generator function.
            
            ### Example module (e.g., `/src/modules/terrain.js`):
            ```js
            export function generateTerrainScale(config) {
              // ...implementation...
              return {
                name: "terrain_scale_8_notes",
                base_frequency: config.baseFrequency,
                notes: [...]
              };
            }
            ```
            
            ### Module manifest (`/src/data/modules.json`):
            ```json
            [
              {
                "id": "terrain",
                "label": "Terrain Scale",
                "type": "generator",
                "entry": "../modules/terrain.js",
                "function": "generateTerrainScale"
              },
              {
                "id": "gap",
                "label": "Gap Scale",
                "type": "generator",
                "entry": "../modules/gap.js",
                "function": "generateGapScale"
              }
            ]
            ```
            
            Modules are auto-loaded and attached to the front-end dropdowns at runtime. **No manual editing of `main` or app code is required.**
            
            ---
            
            ## App Features
            
            - Modular **tool pop-ups** with real-time previews
            - Scrollable and zoomable **multi-scale number line**
            - Bottom **note tray** for collecting and combining notes
            - **Playback engine** using Web Audio API
            - Export any scale or tray as `.json`
            - **Plugin-ready interface** for advanced tools and effects
            
            ---
            
            ## Packaging Options
            
            - **PWA (Progressive Web App)**
              - One-click install on Android
              - Offline-capable
              - Native-like UI and splash screen
            - **APK (Android)**
              - Wrap React frontend using **Capacitor.js**
              - Add native hooks if needed later (e.g. file system)
            
            ---
            
            ## Developer Guidelines
            
            - All core scale logic should live in `/src/modules/` as ES modules.
            - Add new tools by:
              1. Writing the JS module
              2. Updating `modules.json`
            - Shared functions (prime generation, reduction, etc.) go in `/src/utils/`
            - Always export scales to `/output/` so they can be viewed, played, or edited
            
            ---
            
            ## Roadmap Highlights
            
            - [x] Migrate all core algorithms to JavaScript
            - [x] Design final plugin loading system
            - [x] Enable modular UI dropdowns
            - [ ] Add metadata overlay for long-tap previews
            - [ ] Build native APK shell via Capacitor.js
            - [ ] Optional: GitHub-hosted web version for desktop testing
            
            ---
            
            This document now serves as the **canonical reference** for the app's total architecture and frontend goals.
            ```

            `readmes/nextgen_README_consolidated.md`
            ```md
            Prime Scale App – Modular Rewrite (In Progress)
            
            ## Purpose
            This README documents the ongoing modular refactor of the Prime Scale App. Its goal is to offer a clean, scalable, and extensible architecture that supports multiple scale-generation algorithms and prepares the codebase for future CLI, GUI, and web-based interfaces.
            
            ---
            
            ## Project Goals
            - Modular core scale types
            - Reusable utilities for primes, reduction, weighting, and export
            - CLI interface to choose and configure scale types
            - Future-ready for GUI or Web front-end
            
            ---
            
            ## Directory Structure (Target)
            ```
            /prime-scale-app/
            ├── scripts/
            │   ├── core_terrain_scale.py              # Terrain-based density generator
            │   ├── core_gap_scale.py                  # Gap-based note detection (WIP)
            │   ├── core_pure_prime_scale.py           # Raw prime tone sequence
            │   ├── core_cluster_scale.py              # Density-based cluster detection (WIP)
            │   ├── scale_utils.py                     # Shared utilities and exports
            │   ├── main.py                            # CLI entry point (planned)
            │   └── __init__.py                        # Package init
            ├── output/                                # Generated scale .json files
            ├── interface/                             # Optional HTML or GUI code
            ├── README.md                              # Legacy reference
            ├── nextgen_README.md                      # This file – active documentation
            ```
            
            ---
            
            ## Shared Utilities (`scale_utils.py`)
            Implements common functionality:
            - `generate_primes(n)`
            - `reduce_value(val)`
            - `get_log_positions(primes)`
            - `generate_density_axis(resolution)`
            - `circular_distance(a, b)`
            - `prime_weight(p, curve)`
            - `add_bounds(notes, base_freq)` – Adds base and octave markers
            - `export_json(scale_data, filename)` – Saves output to `/output/`
            
            Note: `density_resolution` is included in many modules for future plotting/visualization but may currently be unused. Commented accordingly.
            
            ---
            
            ## Scale Types
            
            ### 1. Terrain-Based Scale (`core_terrain_scale.py`)
            Generates a weighted density map of reduced primes, tiles the log2 octave, and selects either valleys or peaks within segments.
            - Uses gravity-style smoothing for density fade
            - Fully implemented CLI interface
            
            **Arguments**: `--prime-count`, `--base-frequency`, `--num-notes`, `--window-size`, `--density-resolution`, `--mode` (valley/peak), `--include-bounds`, `--weight-curve`
            
            ### 2. Gap-Based Scale (`gap_threshold_scout.py`)
            Scans through gap thresholds between log-reduced primes, selecting gaps that match a target note count.
            - Outputs matching scales to JSON
            - CLI runner implemented
            
            **Arguments**: `--threshold-range`, `--note-goal`, `--tolerance`, `--step-size`, `--prime-count`, `--base-frequency`, `--include-bounds`
            
            Note: `density_resolution` is currently unused (commented).
            
            ### 3. Pure Prime Scale (`core_pure_prime.py`)
            Maps raw reduced primes into pitch space with no filtering.
            - Simplest generator, clean reference
            
            **Arguments**: `--prime-count`, `--base-frequency`, `--include-bounds`, `--density-resolution` *(commented if unused)*
            
            ### 4. Cluster Scale (WIP)
            Combines:
            - `binary_gap_analyzer.py`: Computes binary-segment gaps from reduced primes
            - `cluster_finder.py`: Identifies sparse clusters by filtering gap counts
            
            **Current output is CLI print only – no JSON export yet.**
            
            **Next Steps**:
            - Convert clusters into scale notes
            - Integrate export using `scale_utils.py`
            - Add CLI wrapper for standalone cluster scale
            
            ---
            
            ## Planned CLI Interface (`main.py`)
            Single unified entry point to route commands to different generators.
            
            **Examples:**
            ```sh
            python main.py \
              --scale-type gap \
              --prime-count 2000 \
              --base-frequency 220.0 \
              --gap-threshold 0.012 \
              --sort-by pitch \
              --include-bounds
            
            python main.py \
              --scale-type pure \
              --prime-count 128 \
              --base-frequency 220.0 \
              --order pitch
            
            python main.py \
              --scale-type cluster \
              --prime-count 3000 \
              --base-frequency 220.0 \
              --cluster-sensitivity 0.85 \
              --sort-by strength
            ```
            
            ---
            
            ## Transition Checklist
            
            ### Core Modules:
            - [x] `scale_utils.py` created and shared across all scripts
            - [x] `core_terrain_scale.py` refactored and validated
            - [x] `gap_threshold_scout.py` implemented and debugged
            - [x] `core_pure_prime.py` implemented
            - [ ] `core_cluster_scale.py` to be completed (cluster → note export + CLI)
            
            ### CLI Integration:
            - [ ] Create `main.py` driver with `argparse` routing to each core
            - [ ] Define scale types and attach to handlers in `main.py`
            - [ ] Add validation and unified `--help` messaging
            
            ### Output & Interface:
            - [x] Centralized all JSON exports to `/output/`
            - [ ] GUI or HTML playback (optional – future scope)
            
            ---
            
            ## Notes
            - All scripts use `include_bounds` to optionally add octave anchors.
            - `density_resolution` is present in several modules for consistency, even if not currently used.
            - This file replaces the legacy `README.md` as the living source of documentation.
            - Future additions (e.g. scale metadata, UI metadata flags, performance tweaks) will be tracked here.
            
            ---
            
            ## Dev Guidance
            - Comment out unused arguments (like `density_resolution`) but leave them in place for consistency.
            - Use `scale_utils.py` exclusively for shared logic.
            - Avoid duplicating export or reduction code in core modules.
            - Add CLI wrappers to all future modules.
            
            ---
            
            Let this README grow with the system – all additions should be documented here as they stabilize.
            
            **Next priority: Finish cluster → note export + `main.py` CLI router.**
            ```

            `readmes/prime_scale_cheatsheet_fullpath.txt`
            ```txt
            # PRIME SCALE APP – FULL PATH + MODULE EXECUTION CLI CHEATSHEET
            
            ## TERRAIN SCALE
            cd /storage/emulated/0/Documents/prime-scale-app 
            python -m scripts.main terrain \
              --prime-count 1000 \
              --base-frequency 220.0 \
              --num-notes 8 \
              --window-size 0.007 \
              --density-resolution 4000 \
              --mode valley \
              --weight-curve 1.0 \
              --include-bounds
            
            ## GAP SCALE
            cd /storage/emulated/0/Documents/prime-scale-app
            python -m scripts.main gap --prime-count 1000 --base-frequency 220.0 --threshold-range 0.01 0.05 --step-size 0.001 --note-goal 9 --tolerance 1
            
            ## PURE PRIME SCALE
            cd /storage/emulated/0/Documents/prime-scale-app 
            python -m scripts.main pure \
              --prime-count 128 \
              --base-frequency 220.0 \
              --density-resolution 4000 \
              --include-bounds
            
            ## CLUSTER ANALYSIS (WIP - OUTPUT TO TERMINAL ONLY)
            cd /storage/emulated/0/Documents/prime-scale-app 
            python -m scripts.main cluster \
              --tier 128
            
            ## NOTE:
            # These assume your working directory is set to: /storage/emulated/0/Documents/prime-scale-app
            # If not, cd into that directory or adjust accordingly.
            ```

            `readmes/prime_scale_drive_scripts_README.md`
            ```md
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
            ```

        **scripts/**

            `scripts/__init__.py`
            ```py
            ```

            `scripts/binary_gap_analyzer.py`
            ```py
            import math
            
            def reduce_value(x):
                while x >= 2:
                    x /= 2
                return x
            
            def generate_primes(n):
                primes = []
                candidate = 2
                while candidate <= n:
                    is_prime = True
                    for p in primes:
                        if p * p > candidate:
                            break
                        if candidate % p == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 1
                return primes
            
            def compute_reduced_primes(tier):
                primes = generate_primes(tier)
                reduced = [reduce_value(p) for p in primes]
                return sorted(reduced), primes
            
            def compute_segment_gaps(reduced, tier):
                segment_width = 1 / (tier // 2)
                segments = []
                for i in range(len(reduced) - 1):
                    start = reduced[i]
                    end = reduced[i + 1]
                    gap = end - start
                    segment_count = round(gap / segment_width)
                    segments.append((start, end, segment_count))
                return segments, segment_width
            ```

            `scripts/cluster_finder.py`
            ```py
            import argparse
            from scripts.binary_gap_analyzer import compute_reduced_primes, compute_segment_gaps
            import math
            
            def log_center(start, end):
                return math.sqrt(start * end)
            
            def find_clusters(segments, threshold=4):
                clusters = []
                current_cluster = []
                for start, end, count in segments:
                    if count >= threshold:
                        if current_cluster:
                            clusters.append(current_cluster)
                            current_cluster = []
                    else:
                        current_cluster.append((start, end))
                if current_cluster:
                    clusters.append(current_cluster)
                return clusters
            
            def main():
                parser = argparse.ArgumentParser(description="Cluster Finder based on segment gaps.")
                parser.add_argument("--tier", type=int, required=True, help="Binary segmentation tier (must be power of two)")
                args = parser.parse_args()
            
                reduced, _ = compute_reduced_primes(args.tier)
                segment_data, segment_width = compute_segment_gaps(reduced, args.tier)
            
                clusters = find_clusters(segment_data)
            
                print(f"Tier: {args.tier} | Segment Width: {segment_width:.6f}")
                print(f"Found {len(clusters)} cluster(s):\n")
            
                for idx, cluster in enumerate(clusters):
                    cluster_start = cluster[0][0]
                    cluster_end = cluster[-1][1]
                    center = log_center(cluster_start, cluster_end)
                    print(f"Cluster {idx + 1}:")
                    print(f"  Range: {cluster_start:.6f} -> {cluster_end:.6f}")
                    print(f"  Log Center: {center:.6f}")
                    print(f"  Members: {len(cluster)} segments\n")
            
            if __name__ == "__main__":
                main()
            ```

            `scripts/core_pure_prime_scale.py`
            ```py
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility and visualization
            )
            
            def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
            
                # Optional: generate axis for any future visualization
                _ = generate_density_axis(density_resolution)
            
                notes = []
                for log_pos in log_positions:
                    freq = base_frequency * (2 ** log_pos)
                    notes.append({
                        "log_position": log_pos,
                        "frequency": freq,
                        "midi": round(69 + 12 * math.log2(freq / 440.0)),
                        "cents_from_base": 1200 * log_pos,
                        "prime_sources": []
                    })
            
                if include_bounds:
                    notes = add_bounds(notes, base_frequency)
            
                scale_data = {
                    "name": f"pure_prime_scale_{prime_count}_primes",
                    "base_frequency": base_frequency,
                    "notes": notes
                }
            
                export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_pure_prime_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            ```

            `scripts/core_terrain_scale.py`
            ```py
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                prime_weight,
                circular_distance,
                generate_density_axis,
                add_bounds,
                export_json
            )
            
            # Terrain-specific smoothing function
            def gravitational_fade(d, w, n=2.5):
                relative = d / (w / 2)
                return 1 / (1 + (relative ** n))
            
            # Generate density map across log2-reduced space
            def generate_density_map(log_positions, weights, resolution, window_size):
                x_axis = generate_density_axis(resolution)
                density_map = []
            
                for x in x_axis:
                    total_weight = 0
                    for log_pos, weight in zip(log_positions, weights):
                        distance = circular_distance(log_pos, x)
                        if distance <= window_size / 2:
                            focus = gravitational_fade(distance, window_size)
                            total_weight += weight * focus
                    density_map.append(total_weight)
            
                return x_axis, density_map
            
            # Segment and select notes from density map
            def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                segment_width = 1.0 / num_notes
                selected_notes = []
            
                for i in range(num_notes):
                    segment_start = i * segment_width
                    segment_end = segment_start + segment_width
                    segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
            
                    if segment_range:
                        best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                        freq = base_frequency * (2 ** best_x)
                        selected_notes.append({
                            "log_position": best_x,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * best_x,
                            "prime_sources": []
                        })
            
                return selected_notes
            
            # Full generator function
            def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                weights = [prime_weight(p, weight_curve) for p in primes]
            
                x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
            
                if include_bounds:
                    selected_notes = add_bounds(selected_notes, base_frequency)
            
                scale_data = {
                    "name": f"terrain_scale_{num_notes}_{mode}",
                    "base_frequency": base_frequency,
                    "notes": selected_notes
                }
            
                filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                export_json(scale_data, filename)
            
            # CLI runner
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, default=1000)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--num-notes", type=int, default=8)
                parser.add_argument("--window-size", type=float, default=0.007)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.add_argument("--weight-curve", type=float, default=1.0)
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_terrain_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode,
                    include_bounds=args.include_bounds,
                    weight_curve=args.weight_curve
                )
            ```

            `scripts/gap_threshold_scout.py`
            ```py
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility or plotting if needed
            )
            
            # Count qualifying gaps for a given threshold
            def detect_gap_count(log_positions, threshold):
                log_positions.sort()
                gap_centers = []
            
                for i in range(len(log_positions) - 1):
                    gap = log_positions[i + 1] - log_positions[i]
                    if gap >= threshold:
                        center_log = (log_positions[i] + log_positions[i + 1]) / 2
                        gap_centers.append(center_log)
            
                return gap_centers
            
            # Scan thresholds to find ones that match note goal
            def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                matches = []
            
                # Optional: could use this for visual overlays or precision matching later
                _ = generate_density_axis(density_resolution)
            
                current = threshold_min
                while current <= threshold_max:
                    gap_centers = detect_gap_count(log_positions, current)
                    count = len(gap_centers)
            
                    if abs(count - note_goal) <= tolerance:
                        print(f"✔ Match: {count} notes at threshold {current:.6f}")
                        matches.append((current, count, gap_centers))
                    else:
                        print(f"... Skipped: {count} notes at threshold {current:.6f}")
            
                    current = round(current + step_size, 10)  # Avoid float rounding errors
            
                if matches:
                    best_thresh, best_count, best_centers = matches[0]
                    notes = []
                    for log_pos in best_centers:
                        freq = base_frequency * (2 ** log_pos)
                        notes.append({
                            "log_position": log_pos,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * log_pos,
                            "prime_sources": []
                        })
            
                    if include_bounds:
                        notes = add_bounds(notes, base_frequency)
            
                    scale_data = {
                        "name": f"gap_scout_match_{best_count}_notes",
                        "base_frequency": base_frequency,
                        "notes": notes
                    }
            
                    export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
                else:
                    print("No matching thresholds found within specified range.")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                parser.add_argument("--step-size", type=float, default=0.001)
                parser.add_argument("--note-goal", type=int, required=True)
                parser.add_argument("--tolerance", type=int, default=1)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                scan_thresholds(
                    prime_count=args.prime_count,
                    threshold_min=args.threshold_range[0],
                    threshold_max=args.threshold_range[1],
                    step_size=args.step_size,
                    note_goal=args.note_goal,
                    tolerance=args.tolerance,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            ```

            `scripts/main.py`
            ```py
            """
            Prime Scale App – CLI Entry Point
            
            Usage (run from project root):
              python -m scripts.main --scale-type terrain ...
              python -m scripts.main --scale-type gap ...
              python -m scripts.main --scale-type pure ...
            """
            
            import argparse
            from scripts.core_terrain_scale import generate_terrain_scale
            from scripts.gap_threshold_scout import scan_thresholds
            from scripts.core_pure_prime_scale import generate_pure_prime_scale
            
            def main():
                parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
                subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
            
                # Terrain scale CLI
                terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
                terrain_parser.add_argument("--prime-count", type=int, default=1000)
                terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
                terrain_parser.add_argument("--num-notes", type=int, default=8)
                terrain_parser.add_argument("--window-size", type=float, default=0.007)
                terrain_parser.add_argument("--density-resolution", type=int, default=4000)
                terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
                terrain_parser.set_defaults(include_bounds=True)
            
                # Gap scale CLI
                gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
                gap_parser.add_argument("--prime-count", type=int, required=True)
                gap_parser.add_argument("--base-frequency", type=float, default=220.0)
                gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                gap_parser.add_argument("--step-size", type=float, default=0.001)
                gap_parser.add_argument("--note-goal", type=int, required=True)
                gap_parser.add_argument("--tolerance", type=int, default=1)
                gap_parser.add_argument("--density-resolution", type=int, default=4000)
                gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                gap_parser.set_defaults(include_bounds=True)
            
                # Pure scale CLI
                pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
                pure_parser.add_argument("--prime-count", type=int, required=True)
                pure_parser.add_argument("--base-frequency", type=float, default=220.0)
                pure_parser.add_argument("--density-resolution", type=int, default=4000)
                pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                pure_parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                if args.scale_type == "terrain":
                    generate_terrain_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        num_notes=args.num_notes,
                        window_size=args.window_size,
                        density_resolution=args.density_resolution,
                        mode=args.mode,
                        include_bounds=args.include_bounds,
                        weight_curve=args.weight_curve
                    )
            
                elif args.scale_type == "gap":
                    scan_thresholds(
                        prime_count=args.prime_count,
                        threshold_min=args.threshold_range[0],
                        threshold_max=args.threshold_range[1],
                        step_size=args.step_size,
                        note_goal=args.note_goal,
                        tolerance=args.tolerance,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
                elif args.scale_type == "pure":
                    generate_pure_prime_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
            if __name__ == "__main__":
                main()
            ```

            `scripts/scale_utils.py`
            ```py
            import math
            import json
            import os
            
            def generate_primes(n):
                primes = [2]
                candidate = 3
                while len(primes) < n:
                    is_prime = True
                    for p in primes:
                        if candidate % p == 0:
                            is_prime = False
                            break
                        if p * p > candidate:
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 2
                return primes
            
            def reduce_value(val):
                while val >= 2:
                    val /= 2
                while val < 1:
                    val *= 2
                return val
            
            def get_log_positions(primes):
                """Return log2 positions of primes reduced to the 1–2 octave range."""
                return [math.log2(reduce_value(p)) for p in primes]
            
            def generate_density_axis(resolution):
                """Returns evenly spaced samples from 0 to 1 (not inclusive) for log-space rendering."""
                return [i / resolution for i in range(resolution)]
            
            def circular_distance(a, b):
                return min(abs(a - b), 1 - abs(a - b))
            
            def prime_weight(p, curve=1.0):
                if curve == 0.0:
                    return 1.0
                return 1 / (p ** curve)
            
            def add_bounds(notes, base_freq):
                bounds = [
                    {
                        "log_position": 0.0,
                        "frequency": base_freq,
                        "midi": round(69 + 12 * math.log2(base_freq / 440.0)),
                        "cents_from_base": 0.0,
                        "prime_sources": []
                    },
                    {
                        "log_position": 1.0,
                        "frequency": base_freq * 2,
                        "midi": round(69 + 12 * math.log2((base_freq * 2) / 440.0)),
                        "cents_from_base": 1200.0,
                        "prime_sources": []
                    }
                ]
                return [bounds[0]] + notes + [bounds[1]]
            
            def export_json(scale_data, filename):
                # Always write to top-level /output/ folder
                script_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.dirname(script_dir)
                output_dir = os.path.join(project_root, "output")
            
                os.makedirs(output_dir, exist_ok=True)
                full_path = os.path.join(output_dir, os.path.basename(filename))
            
                with open(full_path, "w", encoding="utf-8") as f:
                    json.dump(scale_data, f, indent=2)
            
                print(f"✔ Saved scale to {full_path}")
            ```

        `viewer.js`
        ```js
        const scaleDisplay = document.getElementById('scale-display');
        
        function loadScale(filename) {
          fetch('output/' + filename)
            .then(res => res.json())
            .then(scale => {
              scaleDisplay.innerHTML = '';
        
              const title = document.createElement('h2');
              title.textContent = scale.name;
              scaleDisplay.appendChild(title);
        
              scale.notes.forEach(note => {
                const btn = document.createElement('button');
                btn.textContent = `${note.frequency.toFixed(2)} Hz`;
                btn.onclick = () => {
                  const ctx = new (window.AudioContext || window.webkitAudioContext)();
                  const osc = ctx.createOscillator();
                  osc.type = 'sine';
                  osc.frequency.value = note.frequency;
                  osc.connect(ctx.destination);
                  osc.start();
                  osc.stop(ctx.currentTime + 0.5);
                };
                scaleDisplay.appendChild(btn);
                scaleDisplay.appendChild(document.createTextNode(` → ${note.cents_from_base.toFixed(2)} cents`));
                scaleDisplay.appendChild(document.createElement('br'));
              });
            })
            .catch(err => {
              scaleDisplay.textContent = 'Failed to load scale file.';
              console.error(err);
            });
        }
        
        // Fetch manifest.json to populate dropdown
        fetch('output/manifest.json')
          .then(res => res.json())
          .then(manifest => {
            const dropdown = document.createElement('select');
            dropdown.onchange = () => loadScale(dropdown.value);
        
            manifest.scales.forEach(file => {
              const option = document.createElement('option');
              option.value = file;
              option.textContent = file;
              dropdown.appendChild(option);
            });
        
            document.body.insertBefore(dropdown, scaleDisplay);
            if (manifest.scales.length > 0) {
              loadScale(manifest.scales[0]);
            }
          })
          .catch(err => {
            scaleDisplay.textContent = 'Failed to load manifest file.';
            console.error(err);
          });
        ```
