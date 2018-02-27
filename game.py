import random

stage = 1
count = 0
level = 1
hd = {}
name = 'Paul'
points = level
score = 0
day = 1
month = 1.00
breached_count = 0
resolved_count = 0


def create_ticket(times):
    global count
    for how_many in range(times):
        if random.randint(1, 3) != 1:
            sev = random.randint(1, 5)
            if sev == 2:
                sev = random.randint(1, 5)
            if sev == 1:
                sev = random.randint(1, 5)
                if sev == 1:
                    sev = random.randint(1, 5)
            tech = random.randint(1, 3)
            if tech == 3:
                tech = random.randint(1, 3)
            if count == 0:
                hd['#'] = ['Status', 'Sev', 'Tech', 'Progress', 'Service Breach']
            count += 1
            hd[str(count)] = ['New', sev, tech, '0/'+str(tech), sev]


def display_hd():
    line = '-' * 57
    print(line)
    text = 'Stage ' + str(stage) + '  Day ' + str(day)
    print(text.center(57))
    print(line)
    if len(hd) == 1:
        for x in hd:
            print('|', str(x).center(3), '|', str(hd[x][0]).center(len(hd['#'][0])), '|', str(hd[x][1]).center(3), '|',
                  str(hd[x][2]).center(4), '|', str(hd[x][3]).center(len(hd['#'][3])), '|',
                  str(hd[x][4]).center(len(hd['#'][4])), '|')
            print(line)
            print("''Work From Home''".center(57))
            print(line)
    else:
        for x in hd:
            print('|', str(x).center(3), '|', str(hd[x][0]).center(len(hd['#'][0])), '|', str(hd[x][1]).center(3), '|',
                  str(hd[x][2]).center(4), '|', str(hd[x][3]).center(len(hd['#'][3])), '|',
                  str(hd[x][4]).center(len(hd['#'][4])), '|')
            print(line)
    display_stats()


def update_progress(ticket_number):
    #  return new progress
    one = int(hd[str(ticket_number)][3][0])
    out_of = hd[str(ticket_number)][3][2]
    one += 1
    return str(one) + '/' + out_of


def add_progress(ticket_number):
    global points
    #  status to WIP and update Progress
    hd[str(ticket_number)][0] = 'WIP'
    hd[str(ticket_number)][3] = update_progress(ticket_number)
    points -= 1


def is_resolved():
    #  if progress is complete, status to Solved, add to score
    global score
    global resolved_count
    for tickets in hd:
        if tickets == '#':
            continue
        one = int(hd[str(tickets)][3][0])
        out_of = int(hd[str(tickets)][3][2])
        if one == out_of and hd[str(tickets)][0] != 'Solved':
            hd[str(tickets)][0] = 'Solved'
            if hd[str(tickets)][1] == 1:
                score += 3
            elif hd[str(tickets)][1] == 2:
                score += 2
            else:
                score += 1
            resolved_count += 1


def update_hd():
    #  if status is Solved, delete ticket from dict
    for ticket in hd.copy():
        if ticket == '#':
            continue
        if hd[str(ticket)][0] == 'Solved' or hd[str(ticket)][0] == 'Breach':
            del hd[str(ticket)]


def is_breached():
    #  is service breached, status to breach and take point
    global score, breached_count
    for ticket in hd:
        if ticket == '#':
            continue
        if hd[str(ticket)][4] == 0:
            hd[str(ticket)][0] = 'Breach'
            breached_count += 1
            score -= 1


def lvl_up():
    line = '-' * 57
    # print(line)
    for i in range(3):
        print('|  LEVELED UP  |  |  LEVELED UP  |  |  LEVELED UP  |'.center(57))
    print(line)


def review():
    line = '-' * 57
    print(line)
    text = '\n\n|  Month Review: Breached: ' + str(breached_count) + ' Resolved: ' + str(resolved_count) + ' |\n\n'
    print(text.center(57))
    #  print(line)


def service_countdown():
    #  reduce service breach by 1
    global score, stage
    global level
    global day
    global month
    for ticket in hd:
        if ticket == '#':
            continue
        hd[str(ticket)][4] -= 1
    day += 1


def display_stats():
    #  display name and points
    line = '-' * 57
    # print(line)
    print('|', 'Name(lvl): ' + str(name) + '(' + str(level) + ')', '|', 'Points:', points, '|',
          'Score:', score)
    print(line)


while True:
    if day / 15 >= month:
        month += 1.00
        stage = int(month)
        review()
    if score >= 10:
        score -= 10
        level += 1
        points = level
        display_hd()
        lvl_up()
    create_ticket(stage)
    display_hd()
    while points > 0:
        ticket_number = input('#')
        if ticket_number == '':
            points = 0
        if ticket_number in hd and hd[str(ticket_number)][0] != 'Breach' and hd[str(ticket_number)][0] != 'Solved':
            add_progress(ticket_number)
            is_resolved()
            display_hd()
    if points == 0:
        #  input('next:')
        service_countdown()
        update_hd()
        is_breached()
        points = level
        continue


