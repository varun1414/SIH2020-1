    Datisdaily=[entry for entry in models.Datisdaily.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today)).values().order_by('-date')]
    
    for item in Datisdaily:
            item.update( {"type":"Datisdaily"})
    Dscndaily=[entry for entry in models.Dscndaily.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today)).values().order_by('-date')]
    
    for item in Datisdaily:
            item.update( {"type":"Dscndaily"})
    Datisweekly=[entry for entry in models.Datisweekly.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today)).values().order_by('-date')]
    # print(Datisweekly)
    for item in Datisweekly:
            item.update( {"type":"Datisweekly"})
    
    
    
    Dscnmonthly=[entry for entry in models.Dscnmonthly.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) ).values()]
    # print(Dscnmonthly)
    for item in Dscnmonthly:
            item.update( {"type":"Dscnmonthly"})        
    
    
    com=Datisdaily+[i for i in Datisweekly]+[i for i in Dscnmonthly]+[i for i in Dscndaily]
    com=sorted(com,key=itemgetter('date'))
    pending=[]
    completed=[]
    error=[]
    comsubmit=0
    comapprove=0
    ncomapprove=0
    for i in com:
        if i['remarks'] != '---Report not submitted---':
            # comsubmitted.append(i)
            
            comsubmit=comsubmit+1
        if i['unit_incharge_approval'] == 'YES':    
            comapprove=comapprove+1
        elif i['unit_incharge_approval'] == 'NO':
            ncomapprove=ncomapprove+1

    # pcount=collections.Counter([d['date'] for d in pending])
    # pend=compute(request,pcount)
    # ccount=collections.Counter([d['date'] for d in completed])
    # comp=compute(request,ccount)
    # ecount=collections.Counter([d['date'] for d in error])
    # err=compute(request,ecount)

    Datisdaily=[entry for entry in models.Datisdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Datisdaily)
    # for item in Datisdaily:
    #         item.update( {"type":"Datisdaily"})
    if Datisdaily == []:
        Datisdaily.append({'dcount':0})
    Datisweekly=[entry for entry in models.Datiswlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Datisweekly)
    if Datisweekly == []:
        Datisweekly.append({'dcount':0})
    # for item in Datisweekly:
    #         item.update( {"type":"Datisweekly"})
    
    
    
    Dscnmonthly=[entry for entry in models.Datismlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date())  & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Dscnmonthly)
    if Dscnmonthly == []:
        Dscnmonthly.append({'dcount':0})

    # for item in Dscnmonthly:
            # item.update( {"type":"Dscnmonthly"})        
    
    
    comlog=Datisdaily[0]['dcount']+Datisweekly[0]['dcount']+ Dscnmonthly[0]['dcount']
    # log=sorted(log,key=itemgetter('date'))
    # print(log)
    comfirsttime_per=(float(comlog)/comsubmit)*100
    sumd=sumw=summ=0
    
    Datisdaily=[entry for entry in models.Datisdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Datisdaily)
    # for item in Datisdaily:
    #         sumd=sumd+item['dcount']
    Datisweekly=[entry for entry in models.Datiswlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Datisweekly)
    # if Datisweekly == []:
    #     Datisweekly.append({'dcount':0})
    # for item in Datisweekly:
    #         sumw=sumw+item['dcount']
    
    
    
    Dscnmonthly=[entry for entry in models.Datismlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Dscnmonthly)
    # if Dscnmonthly == []:
    #     Dscnmonthly.append({'dcount':0})
    # for item in Dscnmonthly:
    #         summ=summ+item['dcount']
    

    commaintain=len(Dscnmonthly)+len(Datisdaily)+len(Datisweekly)
   
    
    sumd=sumw=summ=0
    # surlist = models.DgmReports.objects.filter(Q(r_id=10) | Q(r_id=11) | Q(r_id=14) | Q(r_id=21) | Q(r_id=22) | Q(r_id=23) | Q(r_id=27) |Q(r_id=28) | Q(r_id=) | Q(r_id=30) |Q(r_id=31) |Q(r_id=32))
    
    # for datisd in comlist:
    #     com_labels.append(datisd.r_status)
    #     com_data.append(datisd.r_count)
    
    # print(pend[0][0])

    Datisdaily=[entry for entry in models.Datisdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    print(Datisdaily)
    for item in Datisdaily:
            sumd=sumd+item['dcount']
    Datisweekly=[entry for entry in models.Datiswlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    print(Datisweekly)
    if Datisweekly == []:
        Datisweekly.append({'dcount':0})
    for item in Datisweekly:
            sumw=sumw+item['dcount']
    
    
    
    Dscnmonthly=[entry for entry in models.Datismlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Dscnmonthly)
    if Dscnmonthly == []:
        Dscnmonthly.append({'dcount':0})
    for item in Dscnmonthly:
            summ=summ+item['dcount']

    comrep=sumd+sumw+summ
    commaintain_per=(float(commaintain)/(commaintain + comlog +comrep))*100
    # log=log-rep
    ncomsubmit=len(com)-comsubmit
    print(commaintain)
