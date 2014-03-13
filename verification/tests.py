"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [
                [1, 2],
                [3, 4],
                [1, 5],
                [2, 6],
                [4, 8],
                [5, 6],
                [6, 7],
                [7, 8],
                [6, 10],
                [7, 11],
                [8, 12],
                [10, 11],
                [10, 14],
                [12, 16],
                [14, 15],
                [15, 16]
            ],
            "answer": 3,
            "explanation": [
                [1, 1, 1],
                [6, 2, 2],
                [6, 1, 1]
            ]
        },

        {
            "input": [
                [1, 2],
                [2, 3],
                [3, 4],
                [1, 5],
                [4, 8],
                [6, 7],
                [5, 9],
                [6, 10],
                [7, 11],
                [8, 12],
                [9, 13],
                [10, 11],
                [12, 16],
                [13, 14],
                [14, 15],
                [15, 16]
            ],
            "answer": 2,
            "explanation": [
                [1, 3, 3],
                [6, 1, 1]
            ]
        },

        {
            "input": [
                [1, 2],
                [1, 5],
                [2, 6],
                [5, 6]
            ],
            "answer": 1,
            "explanation": [
                [1, 1, 1]
            ]
        },

        {
            "input": [
                [1, 2],
                [1, 5],
                [2, 6],
                [5, 9],
                [6, 10],
                [9, 10]
            ],
            "answer": 0,
            "explanation": [
            ]
        },

        {
            "input": [
                [16, 15],
                [16, 12],
                [15, 11],
                [11, 10],
                [10, 14],
                [14, 13],
                [13, 9]
            ],
            "answer": 0,
            "explanation": [
            ]
        },

        {
            "input": [
                [3, 4],
                [3, 7],
                [4, 8],
                [7, 8],
                [7, 11]
            ],
            "answer": 1,
            "explanation": [
                [3, 1, 1]
            ]
        },

        {
            "input": [
                [16, 15],
                [16, 12],
                [15, 11],
                [11, 12],
                [11, 10],
                [10, 14],
                [9, 10],
                [14, 13],
                [13, 9],
                [15, 14]
            ],
            "answer": 3,
            "explanation": [
                [9, 1, 1],
                [10, 1, 1],
                [11, 1, 1]
            ]
        },

        {
            "input": [
                [1, 5],
                [5, 9],
                [9, 13],
                [13, 14],
                [2, 3],
                [4, 8],
                [6, 7],
                [6, 10],
                [7, 11],
                [10, 14],
                [14, 15],
                [16, 15],
                [16, 12],
                [8, 12],
                [8, 4],
                [10, 11],
                [11, 15]
            ],
            "answer": 2,
            "explanation": [
                [6, 1, 1],
                [10, 1, 1]
            ]
        },

        {
            "input": [
                [1, 2],
                [3, 2],
                [3, 4],
                [1, 5],
                [2, 6],
                [3, 7],
                [4, 8],
                [5, 9],
                [6, 10],
                [7, 11],
                [8, 12],
                [9, 13],
                [10, 14],
                [11, 15],
                [12, 16],
                [13, 14],
                [15, 14],
                [15, 16]
            ],
            "answer": 1,
            "explanation": [
                [1, 3, 3]
            ]
        },

        {
            "input": [
                [1, 2],
                [3, 2],
                [3, 4],
                [5, 6],
                [9, 10],
                [11, 10],
                [13, 14],
                [15, 14],
                [15, 16],
                [1, 5],
                [9, 5],
                [9, 13],
                [2, 6],
                [3, 7],
                [11, 7],
                [4, 8],
                [12, 8],
                [12, 16]

            ],
            "answer": 3,
            "explanation": [
                [1, 3, 3],
                [1, 1, 1],
                [1, 2, 2]
            ]
        },

        {
            "input": [
                [1, 2],
                [3, 2],
                [3, 4],
                [9, 10],
                [11, 10],
                [13, 14],
                [15, 14],
                [15, 16],
                [1, 5],
                [9, 5],
                [9, 13],
                [3, 7],
                [11, 7],
                [4, 8],
                [12, 8],
                [12, 16],
                [6, 10],
                [6, 7],
                [8, 7],
                [10, 14]

            ],
            "answer": 6,
            "explanation": [
                [1, 3, 3],
                [6, 1, 1],
                [1, 2, 2],
                [6, 2, 2]
            ]
        }

    ],
    "Extra": [
        {
            "input": [
                [1, 2],
                [3, 4],
                [1, 5],
                [2, 6],
                [4, 8],
                [5, 6],
                [7, 8],
                [6, 10],
                [7, 11],
                [8, 12],
                [10, 11],
                [10, 14],
                [12, 16],
                [14, 15],
                [15, 16]
            ],
            "answer": 1,
            "explanation": [
                [1, 1, 1]
            ]
        },

        {
            "input": [
                [1, 2],
                [2, 3],
                [3, 4],
                [1, 5],
                [4, 8],
                [6, 7],
                [5, 9],
                [6, 10],
                [7, 11],
                [8, 12],
                [9, 13],
                [10, 11],
                [12, 16],
                [13, 14],
                [14, 15],
                [15, 16],
                [2, 6],
                [5, 6]
            ],
            "answer": 3,
            "explanation": [
                [1, 3, 3],
                [1, 1, 1],
                [6, 1, 1]
            ]
        },

        {
            "input": [
                [3, 2],
                [3, 7],
                [2, 6],
                [2, 6]
            ],
            "answer": 0,
            "explanation": [
            ]
        },

        {
            "input": [
                [1, 2],
                [1, 5],
                [2, 6],
                [5, 9],
                [6, 10],
                [9, 13],
                [10, 14],
                [13, 14]

            ],
            "answer": 0,
            "explanation": [
            ]
        },

        {
            "input": [
                [8, 7],
                [16, 12],
                [15, 11],
                [3, 2],
                [10, 14],
                [5, 6],
                [13, 9]
            ],
            "answer": 0,
            "explanation": [
            ]
        },

        {
            "input": [
                [3, 4],
                [3, 7],
                [4, 8],
                [7, 8],
                [9, 13]
            ],
            "answer": 1,
            "explanation": [
                [3, 1, 1]
            ]
        },

        {
            "input": [
                [16, 15],
                [16, 12],
                [15, 11],
                [11, 12],
                [11, 10],
                [10, 14],
                [9, 10],
                [14, 13],
                [13, 9],
                [6, 7],
                [10, 6],
                [11, 7]
            ],
            "answer": 3,
            "explanation": [
                [9, 1, 1],
                [6, 1, 1],
                [11, 1, 1]
            ]
        },

        {
            "input": [
                [1, 5],
                [5, 9],
                [9, 13],
                [13, 14],
                [2, 3],
                [4, 8],
                [6, 7],
                [6, 10],
                [7, 11],
                [1, 2],
                [14, 15],
                [16, 15],
                [16, 12],
                [8, 12],
                [8, 4],
                [10, 11],
                [3, 7]
            ],
            "answer": 1,
            "explanation": [
                [6, 1, 1]
            ]
        },

        {
            "input": [
                [1, 2],
                [3, 2],
                [3, 4],
                [1, 5],
                [5, 6],
                [6, 7],
                [8, 7],
                [4, 8],
                [5, 9],
                [9, 10],
                [10, 11],
                [11, 12],
                [8, 12],
                [9, 13],
                [12, 16],
                [13, 14],
                [15, 14],
                [15, 16]
            ],
            "answer": 1,
            "explanation": [
                [1, 3, 3]
            ]
        },

        {
            "input": [
                [1, 2],
                [3, 2],
                [3, 4],
                [5, 6],
                [9, 10],
                [11, 10],
                [13, 14],
                [15, 14],
                [15, 16],
                [1, 5],
                [9, 5],
                [9, 13],
                [3, 7],
                [11, 7],
                [4, 8],
                [12, 8],
                [12, 16]

            ],
            "answer": 2,
            "explanation": [
                [1, 3, 3],
                [1, 2, 2]
            ]
        },
        {
            "input": [
                [1, 2],
                [3, 2],
                [3, 4],
                [9, 10],
                [13, 14],
                [15, 14],
                [15, 16],
                [1, 5],
                [9, 5],
                [9, 13],
                [3, 7],
                [11, 7],
                [4, 8],
                [12, 8],
                [12, 16],
                [6, 10],
                [6, 7],
                [8, 7],
                [10, 14]

            ],
            "answer": 4,
            "explanation": [
                [1, 3, 3],
                [3, 1, 1],
                [9, 1, 1],
                [6, 2, 2]
            ]
        },
        {
            "input": [
                [1, 2],
                [3, 2],
                [3, 4],
                [5, 6],
                [7, 6],
                [8, 7],
                [9, 10],
                [11, 10],
                [11, 12],
                [13, 14],
                [15, 14],
                [15, 16],

                [1, 5],
                [5, 9],
                [9, 13],
                [2, 6],
                [6, 10],
                [14, 10],
                [3, 7],
                [7, 11],
                [11, 15],
                [8, 4],
                [8, 12],
                [12, 16],



            ],
            "answer": 14,
            "explanation": [
                [1, 1, 1],
                [2, 1, 1],
                [3, 1, 1],
                [5, 1, 1],
                [6, 1, 1],
                [7, 1, 1],
                [9, 1, 1],
                [10, 1, 1],
                [11, 1, 1],
            ]
        }
    ]
}
