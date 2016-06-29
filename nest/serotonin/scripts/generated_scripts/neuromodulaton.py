from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()


# Connect the volume transmitter to the parts
vt_dopa_ex = nest.Create('volume_transmitter')
vt_dopa_in = nest.Create('volume_transmitter')
vt_sero_ex = nest.Create('volume_transmitter')
vt_sero_in = nest.Create('volume_transmitter')
DOPA_synparams_ex['vt'] = vt_dopa_ex[0]
DOPA_synparams_in['vt'] = vt_dopa_in[0]
SERO_synparams_ex['vt'] = vt_sero_ex[0]
SERO_synparams_in['vt'] = vt_sero_in[0]


nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)
nest.CopyModel('stdp_serotonine_synapse', sero_model_in, SERO_synparams_in)
nest.CopyModel('stdp_serotonine_synapse', sero_model_ex, SERO_synparams_ex)

nest.Connect(lateralcortex[lateralcortex_5HT][k_IDs], vt_sero_in)
nest.Connect(Basalganglia[Basalganglia_5HT][k_IDs], vt_sero_in)
nest.Connect(entorhinalcortex[entorhinalcortex_5HT][k_IDs], vt_sero_in)
nest.Connect(medialcortex[medialcortex_5HT][k_IDs], vt_sero_in)
nest.Connect(locuscoeruleus[locuscoeruleus_5HT][k_IDs], vt_sero_in)
nest.Connect(locuscoeruleus[locuscoeruleus_5HT][k_IDs], vt_sero_ex)
nest.Connect(locuscoeruleus[locuscoeruleus_DA][k_IDs], vt_dopa_ex)
nest.Connect(ventraltegmentalarea[ventraltegmentalarea_5HT][k_IDs], vt_sero_in)
nest.Connect(ventraltegmentalarea[ventraltegmentalarea_DA][k_IDs], vt_dopa_ex)
nest.Connect(Cerebralcortex[Cerebralcortex_5HT][k_IDs], vt_sero_in)
nest.Connect(Thalamus[Thalamus_5HT][k_IDs], vt_sero_in)
nest.Connect(insularcortex[insularcortex_5HT][k_IDs], vt_sero_in)
nest.Connect(septum[septum_5HT][k_IDs], vt_sero_in)
nest.Connect(hypothalamus[hypothalamus_5HT][k_IDs], vt_sero_in)
nest.Connect(hippocampus[hippocampus_5HT][k_IDs], vt_sero_in)
nest.Connect(neocortex[neocortex_5HT][k_IDs], vt_sero_in)
nest.Connect(DR[DR_5HT][k_IDs], vt_sero_in)
nest.Connect(MnR[MnR_5HT][k_IDs], vt_sero_in)
nest.Connect(pons[pons_5HT][k_IDs], vt_sero_in)
nest.Connect(Periaqueductalgray[Periaqueductalgray_5HT][k_IDs], vt_sero_in)
nest.Connect(prefrontalcortex[prefrontalcortex_5HT][k_IDs], vt_sero_in)
nest.Connect(prefrontalcortex[prefrontalcortex_DA][k_IDs], vt_sero_in)
nest.Connect(striatum[striatum_5HT][k_IDs], vt_dopa_ex)
nest.Connect(striatum[striatum_DA][k_IDs], vt_dopa_ex)
nest.Connect(substantianigra[substantianigra_5HT][k_IDs], vt_sero_in)
nest.Connect(substantianigra[substantianigra_DA][k_IDs], vt_dopa_ex)


connect(lateralcortex[lateralcortex_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Basalganglia[Basalganglia_5HT], Rostralgroup[Rostralgroup_A1], syn_type=SERO_in, weight_coef=1.000000000)
connect(Basalganglia[Basalganglia_5HT], Rostralgroup[Rostralgroup_A2], syn_type=SERO_in, weight_coef=1.000000000)
connect(entorhinalcortex[entorhinalcortex_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(medialcortex[medialcortex_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(locuscoeruleus[locuscoeruleus_5HT], locuscoeruleus[locuscoeruleus_NA], syn_type=SERO_in, weight_coef=1.000000000)
connect(locuscoeruleus[locuscoeruleus_5HT], locuscoeruleus[locuscoeruleus_DA], syn_type=SERO_ex, weight_coef=1.000000000)
connect(locuscoeruleus[locuscoeruleus_DA], DR[DR_5HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_5HT], ventraltegmentalarea[ventraltegmentalarea_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_DA], nucleusaccumbens[nucleusaccumbens_5HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_DA], nucleusaccumbens[nucleusaccumbens_DA], syn_type=DA_ex, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_DA], striatum[striatum_5HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_DA], striatum[striatum_DA], syn_type=DA_ex, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_DA], prefrontalcortex[prefrontalcortex_5HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(ventraltegmentalarea[ventraltegmentalarea_DA], prefrontalcortex[prefrontalcortex_DA], syn_type=DA_ex, weight_coef=1.000000000)
connect(Cerebralcortex[Cerebralcortex_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Cerebralcortex[Cerebralcortex_5HT], striatum[striatum_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Cerebralcortex[Cerebralcortex_5HT], striatum[striatum_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(Cerebralcortex[Cerebralcortex_5HT], substantianigra[substantianigra_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Cerebralcortex[Cerebralcortex_5HT], substantianigra[substantianigra_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(Cerebralcortex[Cerebralcortex_5HT], Basalganglia[Basalganglia_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], medialcortex[medialcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], neocortex[neocortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], lateralcortex[lateralcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], entorhinalcortex[entorhinalcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], prefrontalcortex[prefrontalcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], prefrontalcortex[prefrontalcortex_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], insularcortex[insularcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Thalamus[Thalamus_5HT], Cerebralcortex[Cerebralcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(insularcortex[insularcortex_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(septum[septum_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(septum[septum_5HT], MnR[MnR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(septum[septum_5HT], Rostralgroup[Rostralgroup_A1], syn_type=SERO_in, weight_coef=1.000000000)
connect(septum[septum_5HT], Rostralgroup[Rostralgroup_A2], syn_type=SERO_in, weight_coef=1.000000000)
connect(hypothalamus[hypothalamus_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(hippocampus[hippocampus_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(neocortex[neocortex_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], lateralcortex[lateralcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], entorhinalcortex[entorhinalcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], prefrontalcortex[prefrontalcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], prefrontalcortex[prefrontalcortex_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], septum[septum_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], lateraltegmentalarea[lateraltegmentalarea_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], nucleusaccumbens[nucleusaccumbens_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], nucleusaccumbens[nucleusaccumbens_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], striatum[striatum_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], striatum[striatum_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], bednucleusofthestriaterminalis[bednucleusofthestriaterminalis_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], Thalamus[Thalamus_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], Basalganglia[Basalganglia_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], amygdala[amygdala_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(DR[DR_5HT], hippocampus[hippocampus_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], ventraltegmentalarea[ventraltegmentalarea_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], ventraltegmentalarea[ventraltegmentalarea_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], hypothalamus[hypothalamus_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], Thalamus[Thalamus_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], neocortex[neocortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], medialcortex[medialcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], Cerebralcortex[Cerebralcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], hippocampus[hippocampus_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(MnR[MnR_5HT], insularcortex[insularcortex_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(pons[pons_5HT], MnR[MnR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(Periaqueductalgray[Periaqueductalgray_5HT], MnR[MnR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(prefrontalcortex[prefrontalcortex_5HT], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(prefrontalcortex[prefrontalcortex_DA], DR[DR_5HT], syn_type=SERO_in, weight_coef=1.000000000)
connect(striatum[striatum_5HT], striatum[striatum_DA], syn_type=DA_ex, weight_coef=1.000000000)
connect(striatum[striatum_DA], substantianigra[substantianigra_5HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(striatum[striatum_DA], substantianigra[substantianigra_DA], syn_type=DA_ex, weight_coef=1.000000000)
connect(substantianigra[substantianigra_5HT], substantianigra[substantianigra_DA], syn_type=SERO_in, weight_coef=1.000000000)
connect(substantianigra[substantianigra_DA], nucleusaccumbens[nucleusaccumbens_5HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(substantianigra[substantianigra_DA], nucleusaccumbens[nucleusaccumbens_DA], syn_type=DA_ex, weight_coef=1.000000000)
connect(substantianigra[substantianigra_DA], striatum[striatum_5HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(substantianigra[substantianigra_DA], striatum[striatum_DA], syn_type=DA_ex, weight_coef=1.000000000)


logger.debug("* * * Creating spike generators...")
connect_generator(Thalamus[Thalamus_5HT], startTime=200., stopTime=600., rate=200.000000000, coef_part=1.0)


logger.debug("* * * Attaching spikes detector")
logger.debug("* * * Attaching multimeters")
connect_detector(lateralcortex[lateralcortex_5HT])
connect_multimeter(lateralcortex[lateralcortex_5HT])
connect_detector(Basalganglia[Basalganglia_5HT])
connect_multimeter(Basalganglia[Basalganglia_5HT])
connect_detector(entorhinalcortex[entorhinalcortex_5HT])
connect_multimeter(entorhinalcortex[entorhinalcortex_5HT])
connect_detector(medialcortex[medialcortex_5HT])
connect_multimeter(medialcortex[medialcortex_5HT])
connect_detector(locuscoeruleus[locuscoeruleus_5HT])
connect_multimeter(locuscoeruleus[locuscoeruleus_5HT])
connect_detector(locuscoeruleus[locuscoeruleus_DA])
connect_multimeter(locuscoeruleus[locuscoeruleus_DA])
connect_detector(locuscoeruleus[locuscoeruleus_NA])
connect_multimeter(locuscoeruleus[locuscoeruleus_NA])
connect_detector(ventraltegmentalarea[ventraltegmentalarea_5HT])
connect_multimeter(ventraltegmentalarea[ventraltegmentalarea_5HT])
connect_detector(ventraltegmentalarea[ventraltegmentalarea_DA])
connect_multimeter(ventraltegmentalarea[ventraltegmentalarea_DA])
connect_detector(nucleusaccumbens[nucleusaccumbens_5HT])
connect_multimeter(nucleusaccumbens[nucleusaccumbens_5HT])
connect_detector(nucleusaccumbens[nucleusaccumbens_DA])
connect_multimeter(nucleusaccumbens[nucleusaccumbens_DA])
connect_detector(Cerebralcortex[Cerebralcortex_5HT])
connect_multimeter(Cerebralcortex[Cerebralcortex_5HT])
connect_detector(Thalamus[Thalamus_5HT])
connect_multimeter(Thalamus[Thalamus_5HT])
connect_detector(insularcortex[insularcortex_5HT])
connect_multimeter(insularcortex[insularcortex_5HT])
connect_detector(Rostralgroup[Rostralgroup_A1])
connect_multimeter(Rostralgroup[Rostralgroup_A1])
connect_detector(Rostralgroup[Rostralgroup_A2])
connect_multimeter(Rostralgroup[Rostralgroup_A2])
connect_detector(septum[septum_5HT])
connect_multimeter(septum[septum_5HT])
connect_detector(hypothalamus[hypothalamus_5HT])
connect_multimeter(hypothalamus[hypothalamus_5HT])
connect_detector(hippocampus[hippocampus_5HT])
connect_multimeter(hippocampus[hippocampus_5HT])
connect_detector(lateraltegmentalarea[lateraltegmentalarea_5HT])
connect_multimeter(lateraltegmentalarea[lateraltegmentalarea_5HT])
connect_detector(neocortex[neocortex_5HT])
connect_multimeter(neocortex[neocortex_5HT])
connect_detector(bednucleusofthestriaterminalis[bednucleusofthestriaterminalis_5HT])
connect_multimeter(bednucleusofthestriaterminalis[bednucleusofthestriaterminalis_5HT])
connect_detector(DR[DR_5HT])
connect_multimeter(DR[DR_5HT])
connect_detector(MnR[MnR_5HT])
connect_multimeter(MnR[MnR_5HT])
connect_detector(reticularformation[reticularformation_5HT])
connect_multimeter(reticularformation[reticularformation_5HT])
connect_detector(pons[pons_5HT])
connect_multimeter(pons[pons_5HT])
connect_detector(Periaqueductalgray[Periaqueductalgray_5HT])
connect_multimeter(Periaqueductalgray[Periaqueductalgray_5HT])
connect_detector(prefrontalcortex[prefrontalcortex_5HT])
connect_multimeter(prefrontalcortex[prefrontalcortex_5HT])
connect_detector(prefrontalcortex[prefrontalcortex_DA])
connect_multimeter(prefrontalcortex[prefrontalcortex_DA])
connect_detector(striatum[striatum_5HT])
connect_multimeter(striatum[striatum_5HT])
connect_detector(striatum[striatum_DA])
connect_multimeter(striatum[striatum_DA])
connect_detector(amygdala[amygdala_5HT])
connect_multimeter(amygdala[amygdala_5HT])
connect_detector(substantianigra[substantianigra_5HT])
connect_multimeter(substantianigra[substantianigra_5HT])
connect_detector(substantianigra[substantianigra_DA])
connect_multimeter(substantianigra[substantianigra_DA])


endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=status_gui)