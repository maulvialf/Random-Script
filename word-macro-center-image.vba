Sub CenterInLinePictures()
    Dim i As Long, j As Long
    With ActiveDocument.Range
        For i = 1 To .InlineShapes.Count
            With .InlineShapes(i)
                If .Type <> wdInlineShapeHorizontalLine Then
                    For j = 1 To .Borders.Count
                        .Borders(j).LineStyle = wdLineStyleSingle
                        .Borders(j).Color = wdColorAutomatic
                    Next j
                End If
            End With
        Next i
    End With

  
  Dim objInLineShape As InlineShape
  Dim objDoc As Document
 
  Set objDoc = ActiveDocument
 
  For Each objInLineShape In objDoc.InlineShapes
    objInLineShape.Select
    Selection.ParagraphFormat.Alignment = wdAlignParagraphCenter
  Next objInLineShape
  
End Sub



