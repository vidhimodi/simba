#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

from flask import Flask, request, json

TRENDING_7_DAYS_API = ""
TRENDING_1_MONTH_API = ""
TRENDING_3_MONTHS_API = ""
RECURRING_7_DAYS_API = ""
RECURRING_1_MONTH_API = ""
RECURRING_3_MONTHS_API = ""
REPORT_7_DAYS_API = ""
REPORT_1_MONTH_API = ""
REPORT_3_MONTHS_API = ""



app = Flask(__name__)


@app.route('/', methods=['POST'])
def on_event():
  """Handles an event from Google Chat."""
  event = request.get_json()
  if event['type'] == 'ADDED_TO_SPACE' and not event['space']['singleUserBotDm']:
    text = 'Thanks for adding me to "%s"!' % (event['space']['displayName'] if event['space']['displayName'] else 'this chat')
  elif event['type'] == 'MESSAGE':
    text = 'You said: <br> `%s`' % event['message']['text']
  elif event['type'] == 'CARD_CLICKED':
    if event['action']['actionMethodName'] == 'getTrendingIssues':
      return json.jsonify(
        {"cards": [
          {
            "header": {
              "title": "Trending Issues",
              "subtitle": "Select Duration",
              "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
              "imageStyle": "IMAGE"
            },
            "sections": [
              {
                "widgets": [
                  {
                    "buttons": [
                      {
                        "textButton": {
                          "text": "Last 7 days",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getTrendingIssues7Days"
                            }
                          }
                        }
                      },
                      {
                        "textButton": {
                          "text": "Last 1 month",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getTrendingIssues1Month"
                            }
                          }
                        }
                      },
                      {
                        "textButton": {
                          "text": "Last 3 Months",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getTrendingIssues3Months"
                            }
                          }
                        }
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]})
    elif event['action']['actionMethodName'] == 'getTrendingIssues7Days':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Trending Issues",
          "subtitle": "Last 7 days",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getListOfIssuesInString(TRENDING_7_DAYS_API)
                  }
              }
          ]}]}]})
    elif event['action']['actionMethodName'] == 'getTrendingIssues1Month':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Trending Issues",
          "subtitle": "Last 1 Month",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getListOfIssuesInString(TRENDING_1_MONTH_API)
                  }
              }
          ]}]}]})
    elif event['action']['actionMethodName'] == 'getTrendingIssues3Months':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Trending Issues",
          "subtitle": "Last 3 Months",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getListOfIssuesInString(TRENDING_3_MONTHS_API)
                  }
              }
          ]}]}]})
       
    elif event['action']['actionMethodName'] == 'getReport':
      return json.jsonify(
        {"cards": [
          {
            "header": {
              "title": "Report",
              "subtitle": "Select Duration",
              "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
              "imageStyle": "IMAGE"
            },
            "sections": [
              {
                "widgets": [
                  {
                    "buttons": [
                      {
                        "textButton": {
                          "text": "Last 7 days",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getReport7Days"
                            }
                          }
                        }
                      },
                      {
                        "textButton": {
                          "text": "Last 1 month",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getReport1Month"
                            }
                          }
                        }
                      },
                      {
                        "textButton": {
                          "text": "Last 3 Months",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getReport3Months"
                            }
                          }
                        }
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]})
    elif event['action']['actionMethodName'] == 'getReport7Days':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Report",
          "subtitle": "Last 7 days",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getReport(REPORT_7_DAYS_API)
                  }
              }
          ]}]}]})
    elif event['action']['actionMethodName'] == 'getReport1Month':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Report",
          "subtitle": "Last 1 Month",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getReport(REPORT_1_MONTH_API)
                  }
              }
          ]}]}]})
    elif event['action']['actionMethodName'] == 'getReport3Months':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Report",
          "subtitle": "Last 3 Months",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getReport(REPORT_3_MONTHS_API)
                  }
              }
          ]}]}]})
    elif event['action']['actionMethodName'] == 'getRecurringIssues':
      return json.jsonify(
        {"cards": [
          {
            "header": {
              "title": "Recurring Issues",
              "subtitle": "Select Duration",
              "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
              "imageStyle": "IMAGE"
            },
            "sections": [
              {
                "widgets": [
                  {
                    "buttons": [
                      {
                        "textButton": {
                          "text": "Last 7 days",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getRecurringIssues7Days"
                            }
                          }
                        }
                      },
                      {
                        "textButton": {
                          "text": "Last 1 month",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getRecurringIssues1Month"
                            }
                          }
                        }
                      },
                      {
                        "textButton": {
                          "text": "Last 3 Months",
                          "onClick": {
                            'action':{
                              'actionMethodName':"getRecurringIssues3Months"
                            }
                          }
                        }
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]})
    elif event['action']['actionMethodName'] == 'getRecurringIssues7Days':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Recurring Issues",
          "subtitle": "Last 7 days",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getListOfIssuesInString(RECURRING_7_DAYS_API)
                  }
              }
          ]}]}]})
    elif event['action']['actionMethodName'] == 'getRecurringIssues1Month':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Recurring Issues",
          "subtitle": "Last 1 Month",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getListOfIssuesInString(RECURRING_1_MONTH_API)
                  }
              }
          ]}]}]})
    elif event['action']['actionMethodName'] == 'getRecurringIssues3Months':
      return json.jsonify({"cards": [
        {
          "header": {
          "title": "Recurring Issues",
          "subtitle": "Last 3 Months",
          "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
          "imageStyle": "IMAGE"
        },
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': getListOfIssuesInString(RECURRING_3_MONTHS_API)
                  }
              }
          ]}]}]})
    if event['action']['actionMethodName'] == 'showSimilarMessage':
      return json.jsonify({"cards": [
        {
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': 'Please type: <b>similar "jiraID"</b> <br>Ex: <i>similar ABLL-1234</i>'
                  }
              }
          ]}]}]})
    if event['action']['actionMethodName'] == 'showResolutionMessage':
      return json.jsonify({"cards": [
        {
          "sections": [
          {
            "widgets": [
              {
                'textParagraph': {
                      'text': 'Please type: <b>resolution "jiraID"</b> <br>Ex: <i>resolution ABLL-1234</i>'
                  }
              }
          ]}]}]})

  else:
    return
  return json.jsonify({
  "cards": [
    {
      "header": {
        "title": "Simba Chat Bot",
        "subtitle": "This is subtitle",
        "imageUrl": "https://w7.pngwing.com/pngs/979/165/png-transparent-lion-king-simba-illustration-simba-nala-rafiki-mufasa-the-lion-king-hyena-mammal-cat-like-mammal-animals.png",
        "imageStyle": "IMAGE"
      },
      "sections": [
        {
          "widgets": [
            {
                "keyValue": {
                  "iconUrl": "https://seeklogo.com/images/J/jira-logo-FD39F795A7-seeklogo.com.png",
                  "topLabel": "Jira ID",
                  "content": "ABLL-1234"
                  }
              },
            {
                "keyValue": {
                  "icon": "DESCRIPTION",
                  "topLabel": "Category",
                  "content": "Shared Hosting Linux"
                }
            },
            {
              "buttons": [
                {
                  "textButton": {
                    "text": "Show Trending Issues",
                    "onClick": {
                      'action':{
                        'actionMethodName':"getTrendingIssues"
                      }
                    }
                  }
                },
                {
                  "textButton": {
                    "text": "Show Recurring Issues",
                    "onClick": {
                      'action':{
                        'actionMethodName':"getRecurringIssues"
                      }
                    }
                  }
                },
                {
                  "textButton": {
                    "text": "Generate Report/Analysis",
                    "onClick": {
                      'action':{
                        'actionMethodName':"getReport"
                      }
                    }
                  }
                },
                {
                  "textButton": {
                    "text": "Show Similar Jiras",
                    "onClick": {
                      'action':{
                        'actionMethodName':"showSimilarMessage"
                      }
                    }
                  }
                },
                {
                  "textButton": {
                    "text": "Possible Resolutions by Jira",
                    "onClick": {
                      'action':{
                        'actionMethodName':"showResolutionMessage"
                      }
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

)
def getListOfIssuesInString(simbaServiceAPI):
  return getStringFromList(["ABLL-1234", "ABLL-5678", "ABLL-8765"])

def getStringFromList(inputList):
      joined_string = "<br>".join(inputList)
      return joined_string

def getReport(simbaServiceAPI):
  return "Report yet to be published"

if __name__ == '__main__':
  app.run(port=8080, debug=True)
