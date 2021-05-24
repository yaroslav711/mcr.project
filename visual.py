import plotly.offline
import plotly.graph_objs as go
from datetime import datetime 
import operator
from plotly.subplots import make_subplots
from Parse import git_data, zulip_data, jitsi_data, jitsi_session

dict_git = git_data()['dictionary']
dict_zulip = zulip_data()['dictionary']
# print(dict_zulip)
dict_jitsi = jitsi_data()['dictionary']
dict_session = jitsi_session()['dictionary']
times = sorted(dict_git + dict_zulip + dict_jitsi + dict_session)
git_count, zulip_count, jitsi_count, session_count = [], [], [], []
commits, messages, classes, session  = len(dict_git), len(dict_zulip), len(dict_jitsi), len(dict_session)

def give_mark():
    return round(git_data()['registration'] + zulip_data()['registration'] + (len(dict_git) > 0) + (len(dict_zulip) > 0) + 0.5*(len(jitsi_data()['dictionary']) + len(jitsi_session()['dictionary']) + 0.01))

for time in times:
    # git_count.append(sum(git_count) + dict_git[time])
    # zulip_count.append(sum(zulip_count) + dict_zulip[time])
    if dict_git[time] >= 1: git_count.append(max(git_count) + 1)
    else: git_count.append(max(git_count))
    if dict_zulip[time] >= 1: zulip_count.append(max(zulip_count) + 1)
    else: zulip_count.append(max(zulip_count))
    if dict_jitsi[time] >= 1: jitsi_count.append(max(jitsi_count) + 1)
    else: jitsi_count.append(max(jitsi_count))
    if dict_session[time] <= 1: session_count.append(sum(session_count) + dict_session[time])
    else: session_count.append(sum(session_count) + 1)

def give_count():
    return {'git_count': git_count,
    'zulip_count': zulip_count,
    'jitsi_count': jitsi_count,
    'session_count': session_count
    }

fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.1,
    specs=[[{"type": "scatter"}],
           [{"type": "table"}]]        
)

fig.add_trace(go.Scatter(x=times, y=git_count, name="Gitlab Commits"), row=1, col=1)
fig.add_trace(go.Scatter(x=times, y=zulip_count, name="Zulip messages"), row=1, col=1)
fig.add_trace(go.Scatter(x=times, y=jitsi_count, name="Jitsi classes"), row=1, col=1)
fig.add_trace(go.Scatter(x=times, y=session_count, name="Session classes"), row=1, col=1)

fig.add_trace(
    go.Table(
        header=dict(
            values=['Registration Git', 'Registration Zulip',
                    'Git Commits', 'Jitsi classes', 'Session Classes'],
            line_color='darkslategray',
            fill_color='lightskyblue',
            align="center"
        ),
        cells=dict(
            values=[git_data()['registration'], zulip_data()['registration'],
                 max(give_count()['git_count']), max(give_count()['jitsi_count']),
                  max(give_count()['session_count'])],
            line_color='darkslategray',
            fill_color='lightcyan')
    ),
    row=2, col=1
)


fig.update_layout(
    height=1000,
    xaxis_title = 'Время',
    yaxis_title = 'Активность',
    legend_title = 'Зависимости',
    showlegend=True,
    title_text=f"Москаленко Ярослав              Итоговая оценка: {give_mark()}                {datetime.now()}"
)

plotly.offline.plot(fig, filename='yaamoskalenko.html')  









