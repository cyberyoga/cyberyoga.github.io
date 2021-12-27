

def load_events():
    import yaml

    rooms = {
        'coffee': 'https://kabi.blue/join/coffee/',
        'mate': 'https://kabi.blue/join/mate/',
        'world and stream': 'https://stream.cyberyoga.org/public/club'
    }
    with open('schedule.yaml', 'r') as f:
        events = yaml.safe_load(f)

        # []
        for e in events:
            if not e['description']:
                e['description'] = ""
            e['room_link'] = rooms[e['room']]
        return events
        
from string import Template
table = Template("""
<table class="table table-responsive-xd">
    <thead>
        <tr>
            <th>Time</th>
            <th>Room</th>
            <th>Topic</th>
        </tr>
    </thead>
    <tbody>
        $rows
    </tbody>
</table>
""")



event_row = Template("""<tr>
    <td>$date</td>
    <td><a href="$room_link">$room</a></td>
    <td>
        <span class="fw-bold fs-5">$title</span><br>
        $description
    </td>
</tr>""")

events = load_events()

table_rows = []
for e in events:
    table_rows.append(event_row.substitute(e))

print(table.substitute({'rows':"\n".join(table_rows)}))