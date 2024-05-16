import streamlit as st

st.title("Will RCB qualify?")

rcb_for_initial_runs = 2540
rcb_for_initial_overs = 249.0
rcb_against_initial_runs = 2455
rcb_against_initial_overs = 250.1667

csk_for_initial_runs = 2333
csk_for_initial_overs = 254.6667
csk_against_initial_runs = 2197
csk_against_initial_overs = 254.5

runs_scored_rcb = st.number_input("Runs Scored by RCB",value=180, placeholder="Virat*10?")
runs_scored_csk = st.number_input("Runs Scored by CSK",value=180, placeholder="Will Thala bat?")

overs_rcb = st.number_input("Overs covered by RCB", value=20.0)
overs_csk = st.number_input("Overs covered by CSK", value=20.0)

mathematical_overs_rcb = int(overs_rcb) + (overs_rcb-int(overs_rcb))*0.6667
mathematical_overs_csk = int(overs_csk) + (overs_csk-int(overs_csk))*0.6667

net_run_rate_for_rcb = (rcb_for_initial_runs+runs_scored_rcb)/(rcb_for_initial_overs+mathematical_overs_rcb)
net_run_rate_against_rcb = (rcb_against_initial_runs+runs_scored_csk)/(rcb_against_initial_overs+mathematical_overs_csk)
actual_net_run_rate_rcb = net_run_rate_for_rcb-net_run_rate_against_rcb

net_run_rate_for_csk = (csk_for_initial_runs+runs_scored_csk)/(csk_for_initial_overs+mathematical_overs_csk)
net_run_rate_against_csk = (csk_against_initial_runs+runs_scored_rcb)/(csk_against_initial_overs+mathematical_overs_rcb)
actual_net_run_rate_csk = net_run_rate_for_csk-net_run_rate_against_csk

submit = st.button("Submit", type="primary")

if submit:
  if actual_net_run_rate_rcb>actual_net_run_rate_csk:
    st.write("EEEEE SAAAAALAAA CUP NAAMDEEEEEEE")

  else:
    st.write("THAALAAA IS HERE, sorry RCB Fans!")