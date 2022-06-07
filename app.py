# market classification app
import os
import dash
import torch
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import html
from dash import dcc
from torchmetrics import Precision, Recall, F1Score, Accuracy


DATAPATH = os.path.join("data", "cache")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


def metrics_collection(y_true, y_predict):
    metrics = {
        "Precision": Precision(y_true, y_predict),
        "Recall": Recall(y_true, y_predict),
        "F1": F1Score(y_true, y_predict),
        "Accuracy": Accuracy(y_true, y_predict),
    }
    return metrics


def leftside_figure(ground_truth_image):
    """creates the ground truth image"""
    fig = px.imshow(ground_truth_image.view(28, 28))
    fig.update_layout(title=dict(text="Ground Truth"))
    return fig


def rightside_figure(prediction_image):
    """creates the decoded image"""
    fig = px.imshow(prediction_image.view(28, 28))
    fig.update_layout(title=dict(text="Decoded"))
    return fig


#### DATA ####
predictions_fname = os.path.join("data", "predictions", "predictions.pt")
predictions = torch.load(predictions_fname)
ground_truths_fname = os.path.join("data", "training_split", "val.pt")
ground_truths = torch.load(ground_truths_fname)
sample_idx = 10


#### APP LAYOUT ####
NAVBAR = dbc.NavbarSimple(
    brand="MNIST Encoder-Decoder",
    color="#792ee5",
    dark=True,
    fluid=True,
)

MODEL_CARD = dbc.Card(
    dbc.CardBody(
        [
            html.H4(f"Model Card", id="model_name", className="card-text"),
            html.P(
                f"Some Model Info: {0}",
                id="modelcard_1",
                className="card-text",
                style={"font-size": "80%"},
            ),
            html.P(
                f"Some Model Info: {0}",
                id="modelcard_2",
                className="card-text",
                style={"font-size": "80%"},
            ),
            html.P(
                f"Some Model Info: {0}",
                id="modelcard_3",
                className="card-text",
                style={"font-size": "80%"},
            ),
            html.P(
                f"Some Model Info: {0}",
                id="modelcard_4",
                className="card-text",
                style={"font-size": "80%"},
            ),
        ]
    ),
    className="pretty_container",
)

SIDEBAR = dbc.Col(
    [MODEL_CARD],
    width=3,
)

GROUNDTRUTH = dcc.Graph(
    id="leftside_figure",
    figure=leftside_figure(ground_truths[sample_idx][0]),
    config={
        "responsive": True,  # dynamically resizes Graph with browser winder
        "displayModeBar": True,  # always show the Graph tools
        "displaylogo": False,  # remove the plotly logo
    },
)

PREDICTIONS = dcc.Graph(
    id="rightside_figure",
    figure=rightside_figure(predictions[sample_idx][0]),
    config={
        "responsive": True,  # dynamically resizes Graph with browser winder
        "displayModeBar": True,  # always show the Graph tools
        "displaylogo": False,  # remove the plotly logo
    },
)

SCORES = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.P("Metric 1", style={"font-weight": "bold"}),
                        html.H6(0.01, id="precision-score", style={"font-size": "80%"}),
                    ],
                    id="metric_1",
                    className="mini_container",
                )
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.P("Metric 2", style={"font-weight": "bold"}),
                        html.H6(0.01, id="recall-score", style={"font-size": "80%"}),
                    ],
                    id="metric_2",
                    className="mini_container",
                )
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.P("Metric 3", style={"font-weight": "bold"}),
                        html.H6(0.01, id="f1-score", style={"font-size": "80%"}),
                    ],
                    id="metric_3",
                    className="mini_container",
                )
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.P("Metric 4", style={"font-weight": "bold"}),
                        html.H6(0.01, id="accuracy-score", style={"font-size": "80%"}),
                    ],
                    id="metric_4",
                    className="mini_container",
                )
            ]
        ),
    ],
    id="scores_card",
)

MAIN_AREA = dbc.Col(
    [
        SCORES,
        dbc.Row(
            [
                dbc.Col([GROUNDTRUTH], className="pretty_container", width=5),
                dbc.Col([PREDICTIONS], className="pretty_container", width=5),
            ],
            justify="center",
        ),
    ]
)

BODY = dbc.Container([dbc.Row([SIDEBAR, MAIN_AREA])], fluid=True)

#### PASS LAYOUT TO DASH ####

app.layout = html.Div(
    [
        NAVBAR,
        html.Br(),  # hacky way to create space between header (navbar) and body
        BODY,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
