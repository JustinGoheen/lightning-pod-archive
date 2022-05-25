# market classification app
import os
import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from torchmetrics import Precision, Recall, F1Score, Accuracy
from lightning_pod.network.module import LitModel
from lightning_pod.pipeline.datamodule import LitDataModule
from torchvision import transforms


NETWORKPATH = Path(__file__).parent
PROJECTPATH = NETWORKPATH.parents[0]
DATAPATH = os.path.join(PROJECTPATH, "data", "cache")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


#### HELPER FUNCTIONS ####


def scores_report(y_true, y_predict):

    scores = {
        "Precision": Precision(y_true, y_predict),
        "Recall": Recall(y_true, y_predict),
        "F1": F1Score(y_true, y_predict),
        "Accuracy": Accuracy(y_true, y_predict),
    }

    return scores


def make_model():

    model = LitModel()

    return


def leftside_figure():

    # ground truth
    dataset = LitDataModule().dataset
    dataset = dataset(DATAPATH, download=False, transform=transforms.ToTensor())
    fig = px.imshow(dataset[0][0].view(28, 28))
    fig.update_layout(title=dict(text="Ground Truth"))

    return fig


def rightside_figure():

    # prediction
    dataset = LitDataModule().dataset
    dataset = dataset(DATAPATH, download=False, transform=transforms.ToTensor())
    fig = px.imshow(dataset[1][0].view(28, 28))
    fig.update_layout(title=dict(text="Decoded"))

    return fig


#### APP LAYOUT ####

NAVBAR = dbc.NavbarSimple(
    brand="PyTorch Lightning MNIST Encoder-Decoder",
    color="#792ee5",
    dark=True,
    sticky="top",
)


MODEL_CARD = dbc.Card(
    dbc.CardBody(
        [
            html.P(f"Model: LitModel", id="model_name", className="card-text"),
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
    [html.H4("Model Card"), MODEL_CARD],
    width=3,
)

GROUNDTRUTH = dcc.Graph(
    id="leftside_figure",
    figure=leftside_figure(),
    config={
        "responsive": True,  # dynamically resizes Graph with browser winder
        "displayModeBar": True,  # always show the Graph tools
        "displaylogo": False,  # remove the plotly logo
    },
)

PREDICTIONS = dcc.Graph(
    id="rightside_figure",
    figure=rightside_figure(),
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
                        html.P("Precision", style={"font-weight": "bold"}),
                        html.H6(0.01, id="precision-score", style={"font-size": "80%"}),
                    ],
                    id="R2",
                    className="mini_container",
                )
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.P("Recall", style={"font-weight": "bold"}),
                        html.H6(0.01, id="recall-score", style={"font-size": "80%"}),
                    ],
                    id="RMSE",
                    className="mini_container",
                )
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.P("F1", style={"font-weight": "bold"}),
                        html.H6(0.01, id="f1-score", style={"font-size": "80%"}),
                    ],
                    id="MPD",
                    className="mini_container",
                )
            ]
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.P("Accuracy", style={"font-weight": "bold"}),
                        html.H6(0.01, id="accuracy-score", style={"font-size": "80%"}),
                    ],
                    id="MGD",
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
                dbc.Col(width=1),
                dbc.Col([PREDICTIONS], className="pretty_container", width=5),
            ]
        ),
    ],
    width=9,
)

BODY = dbc.Container([dbc.Row([SIDEBAR, MAIN_AREA])], fluid=True)

#### PASS LAYOUT TO DASH ####

app.layout = html.Div(
    [
        NAVBAR,  # dbc.N
        html.Br(),  # hacky way to create space between header (navbar) and body
        BODY,  # dbc.Container
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
