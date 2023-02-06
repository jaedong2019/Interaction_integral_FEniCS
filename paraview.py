# ===================================
# FEniCS code  
# ===================================
# Post-processing for interation integrale

# author: Xinyuan ZHAI (xinyuan.zhai@ensta-paris.fr)


# trace generated using paraview version 5.9.0-RC2

#### import the simple module from the paraview

from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


a = 3 #Contour coord: control the length of the contour
b = 0.001 #Contour coord: control the height of the contour

foldername = '../CN_AT1_E3000_beta20/' # put your folder path
foldername0 = foldername + 'I_k1.xdmf'
filename = 'I_k1.xdmf'
cellname = 'Energy–momentum tensor'
# create a new 'Xdmf3ReaderS'
j_intxdmf = Xdmf3ReaderS(registrationName=filename, FileName=[foldername0])
j_intxdmf.CellArrays = [cellname]

directory = "k1"
foldername_save = os.path.join(foldername, directory)
os.mkdir(foldername_save)


# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set active source
SetActiveSource(j_intxdmf)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
j_intxdmfDisplay = Show(j_intxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
j_intxdmfDisplay.Representation = 'Surface'
j_intxdmfDisplay.ColorArrayName = [None, '']
j_intxdmfDisplay.SelectTCoordArray = 'None'
j_intxdmfDisplay.SelectNormalArray = 'None'
j_intxdmfDisplay.SelectTangentArray = 'None'
j_intxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
j_intxdmfDisplay.SelectOrientationVectors = 'Energy–momentum tensor'
j_intxdmfDisplay.ScaleFactor = 2.5
j_intxdmfDisplay.SelectScaleArray = 'None'
j_intxdmfDisplay.GlyphType = 'Arrow'
j_intxdmfDisplay.GlyphTableIndexArray = 'None'
j_intxdmfDisplay.GaussianRadius = 0.125
j_intxdmfDisplay.SetScaleArray = [None, '']
j_intxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
j_intxdmfDisplay.OpacityArray = [None, '']
j_intxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
j_intxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
j_intxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
j_intxdmfDisplay.ScalarOpacityUnitDistance = 0.453341265190318
j_intxdmfDisplay.OpacityArrayName = ['CELLS', 'Energy–momentum tensor']

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(j_intxdmfDisplay, ('CELLS', 'Energy–momentum tensor', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
j_intxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
j_intxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Energymomentumtensor_J'
energymomentumtensor_JLUT = GetColorTransferFunction('Energymomentumtensor')

# get opacity transfer function/opacity map for 'Energymomentumtensor_J'
energymomentumtensor_JPWF = GetOpacityTransferFunction('Energymomentumtensor')

# Properties modified on animationScene1
animationScene1.AnimationTime = 1.00001

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# rescale color and/or opacity maps used to exactly fit the current data range
j_intxdmfDisplay.RescaleTransferFunctionToDataRange(False, True)

# show data in view
j_intxdmfDisplay = Show(j_intxdmf, renderView1, 'UnstructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
j_intxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine1.Source.Point1 = [-a, b, 0.0]
plotOverLine1.Source.Point2 = [-a, a, 0.0]

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1.Source)

# set active source
SetActiveSource(plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=plotOverLine1.Source)

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'Energy–momentum tensor'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'Energy–momentum tensor'
plotOverLine1Display.ScaleFactor = 0.09749999996274711
plotOverLine1Display.SelectScaleArray = 'Energy–momentum tensor'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'Energy–momentum tensor'
plotOverLine1Display.GaussianRadius = 0.0048749999981373545
plotOverLine1Display.SetScaleArray = ['POINTS', 'Energy–momentum tensor']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'Energy–momentum tensor']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [-0.0021755730267614126, 0.0, 0.5, 0.0, -7.983796967891976e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [-0.0021755730267614126, 0.0, 0.5, 0.0, -7.983796967891976e-05, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1.Source)

# create a new 'Plot Over Line'
plotOverLine2 = PlotOverLine(registrationName='PlotOverLine2', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine2.Source.Point1 = [-a, a, 0.0]
plotOverLine2.Source.Point2 = [a, a, 0.0]

# show data in view
plotOverLine2Display = Show(plotOverLine2, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine2Display.CompositeDataSetIndex = [0]
plotOverLine2Display.UseIndexForXAxis = 0
plotOverLine2Display.XArrayName = 'arc_length'
plotOverLine2Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesLabelPrefix = ''
plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine2Display
plotOverLine2Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine2Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine2Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine2.Source)

# create a new 'Plot Over Line'
plotOverLine3 = PlotOverLine(registrationName='PlotOverLine3', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine3.Source.Point1 = [a, a, 0.0]
plotOverLine3.Source.Point2 = [a, -a, 0.0]

# show data in view
plotOverLine3Display = Show(plotOverLine3, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine3Display.CompositeDataSetIndex = [0]
plotOverLine3Display.UseIndexForXAxis = 0
plotOverLine3Display.XArrayName = 'arc_length'
plotOverLine3Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesLabelPrefix = ''
plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine3Display
plotOverLine3Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine3Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine3Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine3.Source)

# create a new 'Plot Over Line'
plotOverLine4 = PlotOverLine(registrationName='PlotOverLine4', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine4.Source.Point1 = [a, -a, 0.0]
plotOverLine4.Source.Point2 = [-a, -a, 0.0]

# show data in view
plotOverLine4Display = Show(plotOverLine4, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine4Display.CompositeDataSetIndex = [0]
plotOverLine4Display.UseIndexForXAxis = 0
plotOverLine4Display.XArrayName = 'arc_length'
plotOverLine4Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine4Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine4Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesLabelPrefix = ''
plotOverLine4Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine4Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine4Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine4Display
plotOverLine4Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine4Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine4Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine4.Source)

# create a new 'Plot Over Line'
plotOverLine5 = PlotOverLine(registrationName='PlotOverLine5', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine5.Source.Point1 = [-a, -a, 0.0]
plotOverLine5.Source.Point2 = [-a, -b, 0.0]

# show data in view
plotOverLine5Display = Show(plotOverLine5, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine5Display.CompositeDataSetIndex = [0]
plotOverLine5Display.UseIndexForXAxis = 0
plotOverLine5Display.XArrayName = 'arc_length'
plotOverLine5Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine5Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine5Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine5Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesLabelPrefix = ''
plotOverLine5Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine5Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine5Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine5Display
plotOverLine5Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine5Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine5Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine5Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine5Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine5.Source)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=plotOverLine1)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=2)

# export view
ExportView(foldername_save + '/contour1.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine2)

# create a new 'Integrate Variables'
integrateVariables2 = IntegrateVariables(registrationName='IntegrateVariables2', Input=plotOverLine2)

# show data in view
integrateVariables2Display = Show(integrateVariables2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour2.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine3)

# create a new 'Integrate Variables'
integrateVariables3 = IntegrateVariables(registrationName='IntegrateVariables3', Input=plotOverLine3)

# set active source
SetActiveSource(integrateVariables3)

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView(foldername_save + '/contour3.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine4)

# create a new 'Integrate Variables'
integrateVariables4 = IntegrateVariables(registrationName='IntegrateVariables4', Input=plotOverLine4)

# show data in view
integrateVariables4Display = Show(integrateVariables4, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour4.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine5)

# create a new 'Integrate Variables'
integrateVariables5 = IntegrateVariables(registrationName='IntegrateVariables5', Input=plotOverLine5)

# show data in view
integrateVariables5Display = Show(integrateVariables5, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour5.txt', view=spreadSheetView1, RealNumberPrecision=8)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1823, 898)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraParallelScale = 12.98075498574717

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

#Compute k2###################################


foldername0 = foldername + 'I_k2.xdmf'
filename = 'I_k2.xdmf'
cellname = 'Energy–momentum tensor'
# create a new 'Xdmf3ReaderS'
j_intxdmf = Xdmf3ReaderS(registrationName=filename, FileName=[foldername0])
j_intxdmf.CellArrays = [cellname]

directory = "k2"
foldername_save = os.path.join(foldername, directory)
os.mkdir(foldername_save)


# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set active source
SetActiveSource(j_intxdmf)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
j_intxdmfDisplay = Show(j_intxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
j_intxdmfDisplay.Representation = 'Surface'
j_intxdmfDisplay.ColorArrayName = [None, '']
j_intxdmfDisplay.SelectTCoordArray = 'None'
j_intxdmfDisplay.SelectNormalArray = 'None'
j_intxdmfDisplay.SelectTangentArray = 'None'
j_intxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
j_intxdmfDisplay.SelectOrientationVectors = 'Energy–momentum tensor'
j_intxdmfDisplay.ScaleFactor = 2.5
j_intxdmfDisplay.SelectScaleArray = 'None'
j_intxdmfDisplay.GlyphType = 'Arrow'
j_intxdmfDisplay.GlyphTableIndexArray = 'None'
j_intxdmfDisplay.GaussianRadius = 0.125
j_intxdmfDisplay.SetScaleArray = [None, '']
j_intxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
j_intxdmfDisplay.OpacityArray = [None, '']
j_intxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
j_intxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
j_intxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
j_intxdmfDisplay.ScalarOpacityUnitDistance = 0.453341265190318
j_intxdmfDisplay.OpacityArrayName = ['CELLS', 'Energy–momentum tensor']

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(j_intxdmfDisplay, ('CELLS', 'Energy–momentum tensor', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
j_intxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
j_intxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Energymomentumtensor_J'
energymomentumtensor_JLUT = GetColorTransferFunction('Energymomentumtensor')

# get opacity transfer function/opacity map for 'Energymomentumtensor_J'
energymomentumtensor_JPWF = GetOpacityTransferFunction('Energymomentumtensor')

# Properties modified on animationScene1
animationScene1.AnimationTime = 1.00001

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# rescale color and/or opacity maps used to exactly fit the current data range
j_intxdmfDisplay.RescaleTransferFunctionToDataRange(False, True)

# show data in view
j_intxdmfDisplay = Show(j_intxdmf, renderView1, 'UnstructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
j_intxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine1.Source.Point1 = [-a, b, 0.0]
plotOverLine1.Source.Point2 = [-a, a, 0.0]

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1.Source)

# set active source
SetActiveSource(plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=plotOverLine1.Source)

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'Energy–momentum tensor'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'Energy–momentum tensor'
plotOverLine1Display.ScaleFactor = 0.09749999996274711
plotOverLine1Display.SelectScaleArray = 'Energy–momentum tensor'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'Energy–momentum tensor'
plotOverLine1Display.GaussianRadius = 0.0048749999981373545
plotOverLine1Display.SetScaleArray = ['POINTS', 'Energy–momentum tensor']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'Energy–momentum tensor']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [-0.0021755730267614126, 0.0, 0.5, 0.0, -7.983796967891976e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [-0.0021755730267614126, 0.0, 0.5, 0.0, -7.983796967891976e-05, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1.Source)

# create a new 'Plot Over Line'
plotOverLine2 = PlotOverLine(registrationName='PlotOverLine2', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine2.Source.Point1 = [-a, a, 0.0]
plotOverLine2.Source.Point2 = [a, a, 0.0]

# show data in view
plotOverLine2Display = Show(plotOverLine2, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine2Display.CompositeDataSetIndex = [0]
plotOverLine2Display.UseIndexForXAxis = 0
plotOverLine2Display.XArrayName = 'arc_length'
plotOverLine2Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesLabelPrefix = ''
plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine2Display
plotOverLine2Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine2Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine2Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine2.Source)

# create a new 'Plot Over Line'
plotOverLine3 = PlotOverLine(registrationName='PlotOverLine3', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine3.Source.Point1 = [a, a, 0.0]
plotOverLine3.Source.Point2 = [a, -a, 0.0]

# show data in view
plotOverLine3Display = Show(plotOverLine3, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine3Display.CompositeDataSetIndex = [0]
plotOverLine3Display.UseIndexForXAxis = 0
plotOverLine3Display.XArrayName = 'arc_length'
plotOverLine3Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesLabelPrefix = ''
plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine3Display
plotOverLine3Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine3Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine3Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine3.Source)

# create a new 'Plot Over Line'
plotOverLine4 = PlotOverLine(registrationName='PlotOverLine4', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine4.Source.Point1 = [a, -a, 0.0]
plotOverLine4.Source.Point2 = [-a, -a, 0.0]

# show data in view
plotOverLine4Display = Show(plotOverLine4, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine4Display.CompositeDataSetIndex = [0]
plotOverLine4Display.UseIndexForXAxis = 0
plotOverLine4Display.XArrayName = 'arc_length'
plotOverLine4Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine4Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine4Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesLabelPrefix = ''
plotOverLine4Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine4Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine4Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine4Display
plotOverLine4Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine4Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine4Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine4.Source)

# create a new 'Plot Over Line'
plotOverLine5 = PlotOverLine(registrationName='PlotOverLine5', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine5.Source.Point1 = [-a, -a, 0.0]
plotOverLine5.Source.Point2 = [-a, -b, 0.0]

# show data in view
plotOverLine5Display = Show(plotOverLine5, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine5Display.CompositeDataSetIndex = [0]
plotOverLine5Display.UseIndexForXAxis = 0
plotOverLine5Display.XArrayName = 'arc_length'
plotOverLine5Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine5Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine5Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine5Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesLabelPrefix = ''
plotOverLine5Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine5Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine5Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine5Display
plotOverLine5Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine5Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine5Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine5Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine5Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine5.Source)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=plotOverLine1)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=2)

# export view
ExportView(foldername_save + '/contour1.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine2)

# create a new 'Integrate Variables'
integrateVariables2 = IntegrateVariables(registrationName='IntegrateVariables2', Input=plotOverLine2)

# show data in view
integrateVariables2Display = Show(integrateVariables2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour2.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine3)

# create a new 'Integrate Variables'
integrateVariables3 = IntegrateVariables(registrationName='IntegrateVariables3', Input=plotOverLine3)

# set active source
SetActiveSource(integrateVariables3)

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView(foldername_save + '/contour3.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine4)

# create a new 'Integrate Variables'
integrateVariables4 = IntegrateVariables(registrationName='IntegrateVariables4', Input=plotOverLine4)

# show data in view
integrateVariables4Display = Show(integrateVariables4, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour4.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine5)

# create a new 'Integrate Variables'
integrateVariables5 = IntegrateVariables(registrationName='IntegrateVariables5', Input=plotOverLine5)

# show data in view
integrateVariables5Display = Show(integrateVariables5, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour5.txt', view=spreadSheetView1, RealNumberPrecision=8)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1823, 898)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraParallelScale = 12.98075498574717

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

#Compute J_integrale




foldername0 = foldername + 'I_int.xdmf'
filename = 'I_int.xdmf'
cellname = 'Energy–momentum tensor'
# create a new 'Xdmf3ReaderS'
j_intxdmf = Xdmf3ReaderS(registrationName=filename, FileName=[foldername0])
j_intxdmf.CellArrays = [cellname]

directory = "T-stress"
foldername_save = os.path.join(foldername, directory)
os.mkdir(foldername_save)


# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set active source
SetActiveSource(j_intxdmf)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
j_intxdmfDisplay = Show(j_intxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
j_intxdmfDisplay.Representation = 'Surface'
j_intxdmfDisplay.ColorArrayName = [None, '']
j_intxdmfDisplay.SelectTCoordArray = 'None'
j_intxdmfDisplay.SelectNormalArray = 'None'
j_intxdmfDisplay.SelectTangentArray = 'None'
j_intxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
j_intxdmfDisplay.SelectOrientationVectors = 'Energy–momentum tensor'
j_intxdmfDisplay.ScaleFactor = 2.5
j_intxdmfDisplay.SelectScaleArray = 'None'
j_intxdmfDisplay.GlyphType = 'Arrow'
j_intxdmfDisplay.GlyphTableIndexArray = 'None'
j_intxdmfDisplay.GaussianRadius = 0.125
j_intxdmfDisplay.SetScaleArray = [None, '']
j_intxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
j_intxdmfDisplay.OpacityArray = [None, '']
j_intxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
j_intxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
j_intxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
j_intxdmfDisplay.ScalarOpacityUnitDistance = 0.453341265190318
j_intxdmfDisplay.OpacityArrayName = ['CELLS', 'Energy–momentum tensor']

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(j_intxdmfDisplay, ('CELLS', 'Energy–momentum tensor', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
j_intxdmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
j_intxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Energymomentumtensor_J'
energymomentumtensor_JLUT = GetColorTransferFunction('Energymomentumtensor')

# get opacity transfer function/opacity map for 'Energymomentumtensor_J'
energymomentumtensor_JPWF = GetOpacityTransferFunction('Energymomentumtensor')

# Properties modified on animationScene1
animationScene1.AnimationTime = 1.00001

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# rescale color and/or opacity maps used to exactly fit the current data range
j_intxdmfDisplay.RescaleTransferFunctionToDataRange(False, True)

# show data in view
j_intxdmfDisplay = Show(j_intxdmf, renderView1, 'UnstructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
j_intxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine1.Source.Point1 = [-a, b, 0.0]
plotOverLine1.Source.Point2 = [-a, a, 0.0]

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1.Source)

# set active source
SetActiveSource(plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=plotOverLine1.Source)

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'Energy–momentum tensor'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'Energy–momentum tensor'
plotOverLine1Display.ScaleFactor = 0.09749999996274711
plotOverLine1Display.SelectScaleArray = 'Energy–momentum tensor'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'Energy–momentum tensor'
plotOverLine1Display.GaussianRadius = 0.0048749999981373545
plotOverLine1Display.SetScaleArray = ['POINTS', 'Energy–momentum tensor']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'Energy–momentum tensor']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [-0.0021755730267614126, 0.0, 0.5, 0.0, -7.983796967891976e-05, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [-0.0021755730267614126, 0.0, 0.5, 0.0, -7.983796967891976e-05, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1.Source)

# create a new 'Plot Over Line'
plotOverLine2 = PlotOverLine(registrationName='PlotOverLine2', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine2.Source.Point1 = [-a, a, 0.0]
plotOverLine2.Source.Point2 = [a, a, 0.0]

# show data in view
plotOverLine2Display = Show(plotOverLine2, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine2Display.CompositeDataSetIndex = [0]
plotOverLine2Display.UseIndexForXAxis = 0
plotOverLine2Display.XArrayName = 'arc_length'
plotOverLine2Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine2Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesLabelPrefix = ''
plotOverLine2Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine2Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine2Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine2Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine2Display
plotOverLine2Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine2Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine2Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine2.Source)

# create a new 'Plot Over Line'
plotOverLine3 = PlotOverLine(registrationName='PlotOverLine3', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine3.Source.Point1 = [a, a, 0.0]
plotOverLine3.Source.Point2 = [a, -a, 0.0]

# show data in view
plotOverLine3Display = Show(plotOverLine3, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine3Display.CompositeDataSetIndex = [0]
plotOverLine3Display.UseIndexForXAxis = 0
plotOverLine3Display.XArrayName = 'arc_length'
plotOverLine3Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine3Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesLabelPrefix = ''
plotOverLine3Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine3Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine3Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine3Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine3Display
plotOverLine3Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine3Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine3Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine3.Source)

# create a new 'Plot Over Line'
plotOverLine4 = PlotOverLine(registrationName='PlotOverLine4', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine4.Source.Point1 = [a, -a, 0.0]
plotOverLine4.Source.Point2 = [-a, -a, 0.0]

# show data in view
plotOverLine4Display = Show(plotOverLine4, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine4Display.CompositeDataSetIndex = [0]
plotOverLine4Display.UseIndexForXAxis = 0
plotOverLine4Display.XArrayName = 'arc_length'
plotOverLine4Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine4Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine4Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesLabelPrefix = ''
plotOverLine4Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine4Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine4Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine4Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine4Display
plotOverLine4Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine4Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine4Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(j_intxdmf)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine4.Source)

# create a new 'Plot Over Line'
plotOverLine5 = PlotOverLine(registrationName='PlotOverLine5', Input=j_intxdmf,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine5.Source.Point1 = [-a, -a, 0.0]
plotOverLine5.Source.Point2 = [-a, -b, 0.0]

# show data in view
plotOverLine5Display = Show(plotOverLine5, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine5Display.CompositeDataSetIndex = [0]
plotOverLine5Display.UseIndexForXAxis = 0
plotOverLine5Display.XArrayName = 'arc_length'
plotOverLine5Display.SeriesVisibility = ['Energy–momentum tensor_Magnitude']
plotOverLine5Display.SeriesLabel = ['arc_length', 'arc_length', 'Energy–momentum tensor_X', 'Energy–momentum tensor_X', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Y', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Z', 'Energy–momentum tensor_Magnitude', 'Energy–momentum tensor_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine5Display.SeriesColor = ['arc_length', '0', '0', '0', 'Energy–momentum tensor_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Energy–momentum tensor_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Energy–momentum tensor_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Energy–momentum tensor_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotOverLine5Display.SeriesPlotCorner = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesLabelPrefix = ''
plotOverLine5Display.SeriesLineStyle = ['arc_length', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Energy–momentum tensor_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine5Display.SeriesLineThickness = ['arc_length', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Energy–momentum tensor_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine5Display.SeriesMarkerStyle = ['arc_length', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Energy–momentum tensor_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine5Display.SeriesMarkerSize = ['arc_length', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Energy–momentum tensor_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine5Display
plotOverLine5Display.SeriesPlotCorner = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine5Display.SeriesLineStyle = ['Energy–momentum tensor_Magnitude', '1', 'Energy–momentum tensor_X', '1', 'Energy–momentum tensor_Y', '1', 'Energy–momentum tensor_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine5Display.SeriesLineThickness = ['Energy–momentum tensor_Magnitude', '2', 'Energy–momentum tensor_X', '2', 'Energy–momentum tensor_Y', '2', 'Energy–momentum tensor_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine5Display.SeriesMarkerStyle = ['Energy–momentum tensor_Magnitude', '0', 'Energy–momentum tensor_X', '0', 'Energy–momentum tensor_Y', '0', 'Energy–momentum tensor_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine5Display.SeriesMarkerSize = ['Energy–momentum tensor_Magnitude', '4', 'Energy–momentum tensor_X', '4', 'Energy–momentum tensor_Y', '4', 'Energy–momentum tensor_Z', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# set active source
SetActiveSource(plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine5.Source)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=plotOverLine1)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=2)

# export view
ExportView(foldername_save + '/contour1.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine2)

# create a new 'Integrate Variables'
integrateVariables2 = IntegrateVariables(registrationName='IntegrateVariables2', Input=plotOverLine2)

# show data in view
integrateVariables2Display = Show(integrateVariables2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour2.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine3)

# create a new 'Integrate Variables'
integrateVariables3 = IntegrateVariables(registrationName='IntegrateVariables3', Input=plotOverLine3)

# set active source
SetActiveSource(integrateVariables3)

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView(foldername_save + '/contour3.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine4)

# create a new 'Integrate Variables'
integrateVariables4 = IntegrateVariables(registrationName='IntegrateVariables4', Input=plotOverLine4)

# show data in view
integrateVariables4Display = Show(integrateVariables4, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour4.txt', view=spreadSheetView1, RealNumberPrecision=8)

# set active source
SetActiveSource(plotOverLine5)

# create a new 'Integrate Variables'
integrateVariables5 = IntegrateVariables(registrationName='IntegrateVariables5', Input=plotOverLine5)

# show data in view
integrateVariables5Display = Show(integrateVariables5, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(foldername_save + '/contour5.txt', view=spreadSheetView1, RealNumberPrecision=8)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1823, 898)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraParallelScale = 12.98075498574717

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

#Compute J_integrale



